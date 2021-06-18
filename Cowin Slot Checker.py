from cowin_api import CoWinAPI
import datetime
import sys
from win10toast import ToastNotifier
import time

# <-------------------------------------------- Working Functions -------------------------------------------->


def print_all_states(cowin: CoWinAPI, filename: str = "state_list.csv"):
    '''
    Prints state_ids and state_names in filename

    cowin: the CoWinAPI object
    filename: the filename where you want the state_list to be saved
    '''
    state_list = cowin.get_states()

    default_stdout = sys.stdout

    with open(filename, "w") as f:
        sys.stdout = f
        print("state_id, state_name")
        for state in state_list['states']:
            print(
                f"{state['state_id']} ,{state['state_name']}")

    sys.stdout = default_stdout


def print_all_district(cowin: CoWinAPI, state_id: str, filename: str = "district_list.csv"):
    '''
    Prints District_IDs and District_Names of given state in filename

    cowin: the CoWinAPI Object
    state_id: string which can be found in state_list.csv, defines the unique code given to your state by CoWinAPI
    filename: the filename where you want the district_list to be saved
    '''
    district_list = cowin.get_districts(state_id)

    default_stdout = sys.stdout

    with open(filename, "w") as f:
        sys.stdout = f
        print("district_id, district_name")
        for district in district_list['districts']:
            print(
                f"{district['district_id']} ,{district['district_name']}")

    sys.stdout = default_stdout


def print_all_centers(cowin: CoWinAPI, district_id: str, filename="center_list.csv"):
    '''
    Prints all the centers in the given district in format "pincode, center_id, name"

    cowin: the CoWinAPI Object
    district_id: string which can be found in district_list.csv, defines the unique code given to your district by CoWinAPI
    filename: the filename where you want the center_list to be saved
    '''

    available_centers = cowin.get_availability_by_district(district_id)

    default_stdout = sys.stdout

    with open(filename, "w") as f:
        sys.stdout = f
        print("pincode, center_id, name")
        for center in available_centers['centers']:
            print(
                f"{center['pincode']} ,{center['center_id']}, {center['name']}")

    sys.stdout = default_stdout


def tomorrow() -> str:
    '''
    Gives tomorrow's date in string dd-mm-yyyy format 
    '''
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
    NextDay_Date_Formatted = NextDay_Date.strftime(
        '%d-%m-%Y')  # format the date to dd-mm-yyyy
    return NextDay_Date_Formatted


def today() -> str:
    '''
    Gives today's date in string dd-mm-yyyy format 
    '''
    Day_Date = datetime.datetime.today()
    Day_Date_Formatted = Day_Date.strftime(
        '%d-%m-%Y')  # format the date to dd-mm-yyyy
    return Day_Date_Formatted


def curr_time() -> str:
    '''
    Gives current time in string h-m-s format 
    '''

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time


def look_for_slot(cowin: CoWinAPI, toaster: ToastNotifier, district_id: str, required_center_ids: list[str], minimum_age: int, dose_no: int):
    '''
        Base Function which does the actual work, uses CoWinAPI to get all the center's session in your district_id, then specifically searches in only required_center_ids for available vaccine, if any vaccine slot is found, it give off a Win10 Notification as well as command line verbose

        cowin: the CoWinAPI Object
        toaster: ToastNotifier Object for win10 notification
        district_id: the district_id where you want to search for
        required_center_ids: list of center_ids where you want to look for available vaccine
        minimum_age: the minimum age, enter 18 for 18-45 group and 45 for 45+ group
        dose_no: give 1 for first_dose, 2 for second_dose
    '''
    dates = {today(), tomorrow()}

    for date in dates:
        available_centers = cowin.get_availability_by_district(
            district_id, date, minimum_age)

        for center in available_centers['centers']:
            if(center['center_id'] in required_center_ids):
                for session in center['sessions']:
                    if(dose_no == 1):
                        if(session['available_capacity_dose1'] > 0):
                            print(
                                f"Time: {curr_time()}; Name: {center['name']}; Pincode: {center['pincode']};  Age Limit: {session['min_age_limit']}; Date: {date}; Dose 1 Slots: {session['available_capacity_dose1']}")
                            # showcase
                            toaster.show_toast(
                                "Slot Available",  # title
                                # message
                                f"{center['name']} @ {center['pincode']}\nAge Limit: {session['min_age_limit']}\nDate: {date}\nDose 1 Slots: {session['available_capacity_dose1']}",
                                icon_path=None,  # 'icon_path'
                                duration=5,  # for how many seconds toast should be visible;
                                threaded=True,  # True = run other code in parallel; False = code execution will wait till notification disappears
                            )
                            # Wait for threaded notification to finish
                            while toaster.notification_active():
                                time.sleep(0.1)
                    elif(dose_no == 2):
                        if(session['available_capacity_dose2'] > 0):
                            print(
                                f"Time: {curr_time()}; Name: {center['name']}; Pincode: {center['pincode']}; Age Limit: {session['min_age_limit']}; Date: {date};  Dose 2 Slots: {session['available_capacity_dose2']}")
                            # showcase
                            toaster.show_toast(
                                "Slot Available",  # title
                                # message
                                f"{center['name']} @ {center['pincode']}\nAge Limit: {session['min_age_limit']}\nDate: {date}\nDose 2 Slots: {session['available_capacity_dose2']}",
                                icon_path=None,  # 'icon_path'
                                duration=5,  # for how many seconds toast should be visible;
                                threaded=True,  # True = run other code in parallel; False = code execution will wait till notification disappears
                            )
                            # Wait for threaded notification to finish
                            while toaster.notification_active():
                                time.sleep(0.1)

                    else:
                        raise ValueError("Dose Number Invalid")


def call_fn(cowin: CoWinAPI, toaster: ToastNotifier, district_id: str, required_center_ids: list[str], minimum_age: int = 18,  dose_no: int = 1, refresh_time_min: int = 5):
    '''
        Support Function which calls the base function every refresh_time_min

        cowin: the CoWinAPI Object
        toaster: ToastNotifier Object for win10 notification
        district_id: the district_id where you want to search for
        required_center_ids: list of center_ids where you want to look for available vaccine
        minimum_age: the minimum age, enter 18 for 18-45 group and 45 for 45+ group
        dose_no: give 1 for first_dose, 2 for second_dose
        refresh_time_min: the time the script should wait before rechecking for available doses
    '''
    look_for_slot(cowin, toaster, district_id,
                  required_center_ids, minimum_age, dose_no)
    time.sleep(60*refresh_time_min)


# <-------------------------------------------- Main Code -------------------------------------------->
# initialization
cowin = CoWinAPI()
toaster = ToastNotifier()

# first run the below commented command to get the list of all states and their id's

# print_all_states(cowin)

state_id = '21'
state_name = 'Maharashtra'

# now run the below commented command with your state_id to get all district and their district_ids

# print_all_district(cowin, state_id)

district_id = '395'
district_name = 'Mumbai'

# now run the below commented command with your district_id to get all the centers pincode, center_id, and name

# print_all_centers(cowin, district_id)

# now select make your preferred list of centers to check
required_center_ids = {695695, 597000, 694629}
# not actually required, just for context
required_pin_codes = {400013, 400016, 400028}
# not actually required, just for context
required_names = {"The World Tower MCGM Parkg", "P D Hinduja 1",
                  "KOHINOOR PUB PARKING (DRIVE)"}

# now this will check for all the given centers for any available vaccine slot every refresh_time_min, and will give a win10 notification, if slot found

while True:
    call_fn(cowin, toaster,  district_id,
            required_center_ids, minimum_age=18, dose_no=1,refresh_time_min=1)

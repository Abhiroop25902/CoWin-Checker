from cowin_api import CoWinAPI
import datetime
import sys
from win10toast import ToastNotifier
import time


def print_all_states(cowin: CoWinAPI, filename: str = "state_list.csv"):
    '''Prints state_ids and state_names in filename'''
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
    '''Prints District_IDs and District_Names of given state in filename'''
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
    '''Prints all the centers in the given district in format "pincode, center_id, name"'''

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
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
    NextDay_Date_Formatted = NextDay_Date.strftime(
        '%d-%m-%Y')  # format the date to dd-mm-yyyy
    return NextDay_Date_Formatted


def today() -> str:
    Day_Date = datetime.datetime.today()
    Day_Date_Formatted = Day_Date.strftime(
        '%d-%m-%Y')  # format the date to dd-mm-yyyy
    return Day_Date_Formatted


def curr_time() -> str:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time


def look_for_slot(cowin: CoWinAPI, toaster: ToastNotifier, district_id: str, required_center_ids: list[str], minimum_age: int, dose_no: int):
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
                                f"Name: {center['name']} @ {center['pincode']}\nAge Limit: {session['min_age_limit']}\nDate: {date}\nDose 1 Slots: {session['available_capacity_dose1']}",
                                icon_path=None,  # 'icon_path'
                                duration=10,  # for how many seconds toast should be visible;
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
                                f"Name: {center['name']} @ {center['pincode']}\nAge Limit: {session['min_age_limit']}\nDate: {date}\nDose 2 Slots: {session['available_capacity_dose2']}",
                                icon_path=None,  # 'icon_path'
                                duration=10,  # for how many seconds toast should be visible;
                                threaded=True,  # True = run other code in parallel; False = code execution will wait till notification disappears
                            )
                            # Wait for threaded notification to finish
                            while toaster.notification_active():
                                time.sleep(0.1)

                    else:
                        raise ValueError("Dose Number Invalid")


def call_fn(cowin: CoWinAPI, toaster: ToastNotifier, district_id: str, required_center_ids: list[str], minimum_age: int = 18, refresh_time_min: int = 5, dose_no: int = 1):
    '''Checks for available 1 doses in given centers every 5 minutes'''
    look_for_slot(cowin, toaster, district_id,
                  required_center_ids, minimum_age, dose_no)
    time.sleep(60*refresh_time_min)


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
# not actually required, just for context
required_pin_codes = {400013, 400016, 400028}
required_center_ids = {695695, 597000, 694629}
required_names = {"The World Tower MCGM Parkg", "P D Hinduja 1",
                  "KOHINOOR PUB PARKING (DRIVE)"}  # not actually required, just for context

# now this will check for all the given centers for any available vaccine slot every 10 min, and will give a win10 notification, if found
while True:
    call_fn(cowin, toaster,  district_id,
            required_center_ids, minimum_age=18, dose_no=1)

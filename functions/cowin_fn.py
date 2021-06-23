from cowin_api import CoWinAPI
import sys

from functions import notifier
from functions import utils

cowin = CoWinAPI()


def print_all_states(filename: str = "./data/state_list.csv"):
    '''
    Prints state_ids and state_names in filename

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

    print("Updated state list, see them in './data/state_list.csv'")


def print_all_district(state_id: str, filename: str = "./data/district_list.csv"):
    '''
    Prints District_IDs and District_Names of given state in filename

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

    print(
        f"Updated district list for state_id: {state_id}, see them in './data/district_list.csv'.")


def print_all_centers(district_id: str, filename="./data/center_list.csv"):
    '''
    Prints all the centers in the given district in format "pincode, center_id, name"

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

    print(
        f"Updated center list for district_id: {district_id}, see them in './data/center_list.csv'.")


def check_dose(dose_no:int, center, date):
    '''
    checks for available dose_no in center and date given, gives notification if dose found
    '''
    for session in center['sessions']:
        if(dose_no == 1):
            if(session['available_capacity_dose1'] > 0):
                print(
                    f"Time: {utils.curr_time()}; Name: {center['name']}; Pincode: {center['pincode']};  Age Limit: {session['min_age_limit']}; Date: {date}; Dose 1 Slots: {session['available_capacity_dose1']}")
                notifier.show_notification(
                    f"{center['name']} @ {center['pincode']}\nAge Limit: {session['min_age_limit']}\nDate: {date}\nDose 1 Slots: {session['available_capacity_dose1']}")
        elif(dose_no == 2):
            if(session['available_capacity_dose2'] > 0):
                print(
                    f"Time: {utils.curr_time()}; Name: {center['name']}; Pincode: {center['pincode']}; Age Limit: {session['min_age_limit']}; Date: {date};  Dose 2 Slots: {session['available_capacity_dose2']}")
                notifier.show_notification(
                    f"{center['name']} @ {center['pincode']}\nAge Limit: {session['min_age_limit']}\nDate: {date}\nDose 2 Slots: {session['available_capacity_dose2']}")
        else:
            raise ValueError("Dose Number Invalid")


def look_for_slot(district_id: str, required_center_ids: 'list[str]', minimum_age: int, dose_no: int):
    '''
        Base Function which does the actual work, uses CoWinAPI to get all the center's session in your district_id, then specifically searches in only required_center_ids for available vaccine, if any vaccine slot is found, it give off a Win10 Notification as well as command line verbose

        district_id: the district_id where you want to search for
        required_center_ids: list of center_ids where you want to look for available vaccine, give None to check all centers in district
        minimum_age: the minimum age, enter 18 for 18+ group, 30 for 30+ group and 45 for 45+ group
        dose_no: give 1 for first_dose, 2 for second_dose
    '''
    dates = {utils.today(), utils.tomorrow()}

    for date in dates:
        available_centers = cowin.get_availability_by_district(
            district_id, date, minimum_age)

        for center in available_centers['centers']:
            if(required_center_ids == None):
                check_dose(dose_no, center, date)
            else:
                if(center['center_id'] in required_center_ids):
                    check_dose(dose_no, center, date)
                
                    

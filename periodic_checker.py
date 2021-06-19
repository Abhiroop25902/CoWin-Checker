import cowin_fn
import time


def start_check(district_id: str, lookup_center_ids: list[str], minimum_age: int = 18, dose_no: int = 1, refresh_time_min: int = 5):
    '''
    Start the checker, which checks periodically for available vaccines in lookup_center_ids, and gives notification if any vaccine_slot found

    district_id: the district_id where you want to search for
    lookup_center_ids: list of center_ids where you want to look for available vaccine
    minimum_age: the minimum age, enter 18 for 18+ group, 30 for 30+ group, and 45 for 45+ group
    dose_no: give 1 for first_dose, 2 for second_dose
    refresh_time_min: the time the script should wait before rechecking for available doses
    '''
    while True:
        cowin_fn.look_for_slot(district_id,
                               lookup_center_ids, minimum_age, dose_no)
        time.sleep(60*refresh_time_min)

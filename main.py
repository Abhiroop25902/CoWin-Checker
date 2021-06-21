from setup import district_id, specific_center_ids
from functions import periodic_checker

# now this will check for all the given centers for any available vaccine slot every refresh_time_min, and will give a win10 notification, if slot found
periodic_checker.start_check(
    district_id, specific_center_ids, minimum_age=45, dose_no=2, refresh_time_min=1)

from functions import cowin_fn
from functions import periodic_checker

# <-------------------------------------------- Main Code -------------------------------------------->
# initialization

# first run the below commented command to get the list of all states and their id's

# cowin_fn.print_all_states()

state_id = '21'
state_name = 'Maharashtra'

# now run the below commented command with your state_id to get all district and their district_ids

# cowin_fn.print_all_district(state_id)

district_id = '395'
district_name = 'Mumbai'

# now run the below commented command with your district_id to get all the centers pincode, center_id, and name

# cowin_fn.print_all_centers(district_id)

# now select make your preferred list of centers to check
required_center_ids = {695695, 597000, 694629}
# not actually required, just for context
required_pin_codes = {400013, 400016, 400028}
# not actually required, just for context
required_names = {"The World Tower MCGM Parkg", "P D Hinduja 1",
                  "KOHINOOR PUB PARKING (DRIVE)"}

# now this will check for all the given centers for any available vaccine slot every refresh_time_min, and will give a win10 notification, if slot found
periodic_checker.start_check(
    district_id, required_center_ids, minimum_age=18, dose_no=1, refresh_time_min=1)

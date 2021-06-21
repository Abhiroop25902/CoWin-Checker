from functions import cowin_fn

# first run the below command to get the list of all states and their id's

cowin_fn.print_all_states()

state_id = '21'
state_name = 'Maharashtra'

# now run the below command with your state_id to get all district and their district_ids

cowin_fn.print_all_district(state_id)

district_id = '395'
district_name = 'Mumbai'

# now run the below commented command with your district_id to get 
# all the centers pincode, center_id, and name

cowin_fn.print_all_centers(district_id)

# now select make your preferred list of centers to check
specific_center_ids = {695695, 597000, 694629}
specific_pin_codes = {400013, 400016, 400028}
specific_names = {"The World Tower MCGM Parkg", "P D Hinduja 1",
                  "KOHINOOR PUB PARKING (DRIVE)"}


print(f"state_id: {state_id}\nstate: {state_name}")
print(f"district_id: {district_id}\ndistrict: {district_name}")

for center_id,pincode,name in zip(specific_center_ids,specific_pin_codes,specific_names):
    print(f"center_id: {center_id}; pincode: {pincode}; center_name: {name}")

print("If any of these information is wrong, please update your information in 'setup.py'.\n")

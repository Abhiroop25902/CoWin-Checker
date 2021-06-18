# CoWin-Checker

I am unhappy with Telegram Bots showing only paid vaccines, so I made my hands dirty and made myself this script.

What this script does is that it uses CoWinAPI to check specific centers periodically and gives a Win10 notification if it finds any available slots.

Thanks to [@backtrackbaba](https://github.com/backtrackbaba) for providing [CoWin API Wrapper](https://github.com/backtrackbaba/cowin) for python

Thanks to [@jithurjacob](https://github.com/jithurjacob) for providing [Win10 Toast Notification Interface](https://github.com/jithurjacob/Windows-10-Toast-Notifications) for python

## How to use this script

1.  Fork This Repo and Clone it in your local computer
2.  Open `Cowin Slot Checker.py` and do the first time setup
    1. Comment following line, this calls the main working code, which is useful only after all the setup procedure.
        ```python
        # now this will check for all the given centers for any available vaccine slot every refresh_time_min, 
        # and will give a win10 notification, if slot found

        while True:                                                                     #<------------------
            call_fn(cowin, toaster,  district_id,                                       #<------------------
                    required_center_ids, minimum_age=18, dose_no=1, refresh_time_min=1) #<------------------

        ```
    2.  Uncomment the following line and run script to update `state_list.csv`, and consequently update the `state_id` to match with your state, re-comment this line again after setup.
           
        ```python
        # first run the below commented command to get the list of all states and their id's

        # print_all_states(cowin) <------------------

        state_id = '21'
        ```
    3. Uncomment the following line and run script to update `district_list.csv`, and consequently update the `district_id` to match with your district, re-comment this line again after setup
        ```python
        # now run the below commented command with your state_id to get all district and their district_ids

        # print_all_district(cowin, state_id) <------------------

        district_id = '395'
        ```
    4. Uncomment the following line and run script to update `center_list.csv`, and consequently update the `required_center_ids` to match with your the centers you want the script to watch, re-comment this line again after setup
        ```python
        # now run the below commented command with your district_id to get all the centers pincode, center_id, and name

        # print_all_centers(cowin, district_id) <------------------

        # now select make your preferred list of centers to check
        required_center_ids = {695695, 597000, 694629}
        ```
    5. Now your setup is over, uncomment the main working code
        ```python
        # now this will check for all the given centers for any available vaccine slot every refresh_time_min, 
        # and will give a win10 notification, if slot found

        while True:                                                                   
            call_fn(cowin, toaster,  district_id,                                       
                    required_center_ids, minimum_age=18, dose_no=1, refresh_time_min=1)

        ```
        1. Here `minimum_age` is the age bracket you want to search for, for 18-45 group keep this 18, for 45+ group, keep this 45
        2. Here `dose_no` signifies 1st dose or 2nd dose, keep this 1 for first dose search, keep this 2 for second dose search
        3. Here `refresh_time_min` signifies the amount of minutes to wait before rechecking for available slots, please care for CoWin Servers and not give this as 0 😅

3. Now all the setup are over, now I suggest you to close the editor, and open a powershell window, go to the folder of script and do the following

```powershell
PS file_directory> python '.\Cowin Slot Checker.py'
```
4.  This will run the script in the powershell window, and will ping you if there is any available vaccine slot
    -   This script takes 21 MB RAM in my system. If by any chance if starts consuming abnormally high amount of RAM, close the command immediately and give me a issue 😅.
    -   To Stop this script, go to powershell and do `Ctrl+C` repeatedly till the process gets stopped (I know 😅)
    -   Do not close powershell window, while this is being executed hoping that it will happen in background, Windows doesn't allows this, and will automatically close the script once powershell windows get closed.

## Future Plans
1. Make Setup Procedure Simpler
2. Add GUI, or convert this to full-fledged service
3. Make the script Operating System Independent

# CoWin-Checker

I am unhappy with Bots showing only paid vaccines, so I made my hands dirty and made myself this script.

What this script does is that it uses CoWinAPI to check specific centers periodically and gives a Win10 notification if it finds any available slots.

Thanks to [@backtrackbaba](https://github.com/backtrackbaba) for [CoWin API Wrapper](https://github.com/backtrackbaba/cowin) for python

Thanks to [@ms7m](https://github.com/ms7m) for providing [Cross Platform Notification Module](https://github.com/ms7m/notify-py) for python

## How to use this script

1.  Fork This Repo and Clone it in your local computer
2.  Install dependencies
    ```shell
    pip install cowin
    pip install notify-py
    ```
3.  Open `setup.py` and do the first time setup

    1. Find your state and state_id from `./data/state_list.csv`, and update `state_id` and `state_name` to match with your state.

        ```python
        # first run the below command to get the list of all states and their id's

        cowin_fn.print_all_states()

        state_id = '21'             #<----
        state_name = 'Maharashtra'  #<----
        ```

    2. Find your district and district_id from `./data/district_list.csv`, and update `district_id` and `district_name` to match with your district.

        ```python
        # now run the below command with your state_id to get all district and their district_ids

        cowin_fn.print_all_district(state_id)

        district_id = '395'         #<----
        district_name = 'Mumbai'    #<----
        ```

    3. Uncomment the following line and run script to update `./data/center_list.csv`, and consequently update the `required_center_ids` to match with your the centers you want the script to watch, re-comment this line again after setup

        ```python
        # now run the below commented command with your district_id to get
        # all the centers pincode, center_id, and name

        cowin_fn.print_all_centers(district_id)

        # now select make your preferred list of centers to check
        specific_center_ids = {695695, 597000, 694629}                     #<---
        specific_pin_codes = {400013, 400016, 400028}                      #<---
        specific_names = {"The World Tower MCGM Parkg", "P D Hinduja 1",   #<---
                        "KOHINOOR PUB PARKING (DRIVE)"}                    #<---
        ```

4.  Now your setup is over, head over to `main.py`

    ```python
    # now this will check for all the given centers for any available vaccine
    # slot every refresh_time_min, and will give a win10 notification,
    # if slot found
    periodic_checker.start_check(
        district_id, specific_center_ids, minimum_age=45, dose_no=2, refresh_time_min=1)
    ```

    1. Here `minimum_age` is the age bracket you want to search for, enter 18 for 18+ group, 30 for 30+ group, and 45 for 45+ group
    2. Here `dose_no` signifies 1st dose or 2nd dose, keep this 1 for first dose search, keep this 2 for second dose search
    3. Here `refresh_time_min` signifies the amount of minutes to wait before rechecking for available slots, please care for CoWin Servers and not give this as 0 ????

5.  Now all the setup are over, now I suggest you to close the editor, and open terminal window, go to the folder of script and do the following

    ```shell
    python main.py
    ```

6.  This will run the script in the powershell window, and will ping you if there is any available vaccine slot
    -   This script takes 21 MB RAM in my system. If by any chance if starts consuming abnormally high amount of RAM, close the command immediately and give me a issue ????.
    -   To Stop this script, go to terminal and do `Ctrl+C` repeatedly till the process gets stopped (I know ????)
    -   Do not close terminal window, while this is being executed hoping that it will happen in background, Windows doesn't allows this , and will automatically close the script once powershell windows get closed. (No idea about Linux or MacOS)

## Future Plans

1. Try to website deploy/ Discord/ Telegram Bot
2. Add GUI, or convert this to full-fledged service

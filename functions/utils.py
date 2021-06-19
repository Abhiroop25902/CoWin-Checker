import datetime
import time


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

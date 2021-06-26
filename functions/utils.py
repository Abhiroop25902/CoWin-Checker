import datetime
import time

def curr_time() -> str:
    '''
    Gives current time in string h-m-s format 
    '''

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

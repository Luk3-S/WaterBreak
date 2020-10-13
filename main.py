import os
from datetime import datetime, time, timedelta
from reminderWindow import *
import time


def build_parameters(path):
    cfg = open(path)
    params = {}
    remind_intervals =[]

    ## aquire parameters from file
    for i in cfg:
        l = i.replace("\n","")
        line = l.split(",")

        params[line[0]] = line[1:]
        remind_intervals.append(line[1])
   
    return params,remind_intervals


def is_time_between(begin_time, end_time, check_time=None):
    #code from https://stackoverflow.com/questions/10048249/how-do-i-determine-if-current-time-is-within-a-specified-range-using-pythons-da
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time




def generate_reminders(remind_intervals,params):

    
    for k,v in params.items():
        reminder_info = []
        endtime = datetime(100,1,1,17,30,00)
        curr = datetime(100,1,1,8,30,00)
        while (curr < endtime):
            curr = curr + timedelta(minutes=int(v[0]))
            reminder_info.append(curr.time())
        v.append(reminder_info)
   


if __name__ == "__main__":
    params,remind_intervals = build_parameters(os.getcwd()+"/config.csv")    
    generate_reminders(remind_intervals,params)

    to_call = {}
    to_rmv =[]
    while (1==1):
        for k,v in params.items():

            for i in range(len(v[len(v)-1])):
                #print(i)
                current = datetime.now()
                leeway = current + timedelta(minutes=30)
                current =current.time()
                leeway=leeway.time()

                #check if current time is within a certain leeway or equal to a reminder time 
                if (is_time_between(current,leeway,v[len(v)-1][i]) or v[len(v)-1][i] == datetime.now().time()):
                    to_call[k] = v[:len(v)-1]
                    to_rmv.append(i)

            print("v after: {}".format(v))
            print("to_call: {}".format(to_call)) 
            print(to_rmv)  
            for i in to_rmv:
                print("i: ",i)
                print("vlen ",v[len(v)-1][i])
                del v[len(v)-1][i]
            to_rmv=[]
        if (len(to_call)>0):
            generatePopup(to_call)
        to_call = {}
        #time.sleep(180)
        time.sleep(60)
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
    
    # for k,v in params.items():
    #     print (k,v)
    # for i in remind_intervals:
    #     print(i)
    return params,remind_intervals


def is_time_between(begin_time, end_time, check_time=None):
    #code from https://stackoverflow.com/questions/10048249/how-do-i-determine-if-current-time-is-within-a-specified-range-using-pythons-da
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        #print("check | beg | end")
        #print("{},{},{}".format(check_time,begin_time,end_time))
        #print(check_time >= begin_time and check_time <= end_time)
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time


#run code continually throughout the working day

#params: 
# parameter: remindPeriod, other parameter
params,remind_intervals = build_parameters(os.getcwd()+"/config.csv")



#while (is_time_between(time(8,30), time(17,00))):
# start = time(8,30)
# next_reminder = []



def generate_reminders(remind_intervals,params):

    
    for k,v in params.items():
        reminder_info = []
        endtime = datetime(100,1,1,17,30,00)
        curr = datetime(100,1,1,8,30,00)
        while (curr < endtime):
            #print("k: {} ,v: {}".format(k,v[0]))
            curr = curr + timedelta(minutes=int(v[0]))
            reminder_info.append(curr.time())
        v.append(reminder_info)
        #print(v)
        #print("\n")
    
    
generate_reminders(remind_intervals,params)


#while (1==1):

to_call = {}
while (1==1):
    for k,v in params.items():

        #to_remove =[]
        #print ("\n")
        #print(k,v)
        
        #print(v)
        # print("arg:")
        # print(v[len(v)])
        # print("now:")
        # print(datetime.now().time())
        for i in range(len(v[len(v)-1])):
            #print(i)
            current = datetime.now()
            leeway = current + timedelta(minutes=3)
            current =current.time()
            leeway=leeway.time()
            #print(leeway)
            #check if current time is within a certain leeway or equal to a reminder time 
            if (is_time_between(current,leeway,v[len(v)-1][i]) or v[len(v)-1][i] == datetime.now().time()):
                #to_call.append("{}: {}".format(k,v[len(v)-1][i]))
                #to_call.append("{}, {}".format(k,v[:len(v)-1]))
                to_call[k] = v[:len(v)-1]
                



        print("v after: {}".format(v))
        print("to_call: {}".format(to_call))   
    

    if (len(to_call)>0):
        generatePopup(to_call)
    to_call = {}
    time.sleep(180)


import time,keyboard
from datetime import datetime
from math import inf
from playsound import playsound
def timer():
    try:
        n=int(input("enter seconds"))
        if(n<0):
            print("not a valid time")
        i=n
        while i>=0:
            if(i==0):
                playsound(r'C:\Users\91829\OneDrive\Desktop\coding\Timer project\Sounds\winfantasia-6912.mp3')
            print(i)
            playsound(r'C:\Users\91829\OneDrive\Desktop\coding\Timer project\Sounds\click-button-140881.mp3')
            time.sleep(0.8)
            i-=1
    except:
        print("An error occured please try again")
def stopwatch():
    print("Press G and enter to start")
    print("press s to stop")
    e=input()
    if(e.lower()=='g'):
        i=0
        while i<=inf:
            if keyboard.is_pressed('s'):
                print("stopped")
                break
            else:
                time.sleep(0.09)
                print(round(i,3))
                i+=0.1
        input("Press enter to quit")
def alarm():
    alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
    alarm_hour=alarm_time[0:2]
    alarm_minute=alarm_time[3:5]
    alarm_seconds=alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()
    print("Setting up alarm..")
    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")
        if(alarm_period==current_period):
            if(alarm_hour==current_hour):
                if(alarm_minute==current_minute):
                    if(alarm_seconds==current_seconds):
                        print("Wake Up!")
                        playsound(r'C:\Users\91829\OneDrive\Desktop\coding\Timer project\Sounds\smartphone_vibrating_alarm_silent-7040.mp3')
                        break
op=int(input("enter the one of the options\n1)Timer\n2)Stop watch\n"))
match op:
    case 1:
        timer()
    case 2:
        stopwatch()
    case 3:
        alarm()
    case _:
        print("Invalid option")

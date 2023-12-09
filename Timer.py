import time,keyboard
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
            time.sleep(1)
            i-=1
    except:
        print("An error occured please try again")
def stopwatch():
    print("Press G and enter to start")
    print("press s to Reset")
    e=input()
    if(e.lower()=='g'):
        i=0
        while i<=inf:
            if keyboard.is_pressed('s'):
                print("stopped")
                break
            else:
                time.sleep(0.1)
                print(round(i,3))
                i+=0.1
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

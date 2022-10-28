import serial
from time import sleep
from IPython.display import clear_output

import RPi.GPIO as GPIO
import time

import RPi.GPIO as GPIO
import time as time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
 
pwm = GPIO.PWM(12, 50) # GPIO18, frequency=50Hz
pwm.start(0)



a=[]

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
while True:
    global a
    received_data = ser.read()              #read serial port
    sleep(0.1)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data.rstrip(),flush=True)                   #print received data
    ser.write(received_data)                #transmit data serially 
    # clear_output(wait=True)
    a.append(received_data)
    if a[0]== b'right':
        received_data = ser.read()              #read serial port
        sleep(0.1)
        data_left = ser.inWaiting()             #check for remaining byte
        received_data += ser.read(data_left)
        print (received_data.rstrip(),flush=True)                   #print received data
        ser.write(received_data)                #transmit data serially 
        # clear_output(wait=True)
        a.append(received_data)
        
        pwm.ChangeDutyCycle(30)
        time.sleep(int(a[1]))
        pwm.ChangeDutyCycle(0)
    
        print("end")
    elif a[0]== b'left':
        received_data = ser.read()              #read serial port
        sleep(0.1)
        data_left = ser.inWaiting()             #check for remaining byte
        received_data += ser.read(data_left)
        print (received_data.rstrip(),flush=True)                   #print received data
        ser.write(received_data)                #transmit data serially 
        # clear_output(wait=True)
        a.append(received_data)
        
        pwm.ChangeDutyCycle(30)
        time.sleep(int(a[1]))
        pwm.ChangeDutyCycle(0)
        
    print(a)
    a=[]
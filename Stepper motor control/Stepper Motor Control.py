#Modules 
from goto import *
import time 
import RpiMotorLib
import RPi.GPIO as GPIO
# Peripheral Configuration Code (do not edit) #CONFIG_BEGIN
def peripheralSetup(): 
#Peripheral Constructors
#Install interrupt handlers
    pass
def peripheralLoop():
    pass
#CONFIG END-

#Main function
peripheralSetup()
D1=22
D2=23
D3=24
D4=25
def Setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(D1,GPIO.OUT)
    GPIO.setup(D2,GPIO.OUT) 
    GPIO.setup(D3,GPIO.OUT) 
    GPIO.setup(D4,GPIO.OUT)

def turnUp():
    GPIO.output(D1,GPIO.HIGH)
    GPIO.output(D2,GPIO.LOW)
    GPIO.output(D3,GPIO.LOW)
    GPIO.output(D4,GPIO.HIGH)

def turnDown():
    GPIO.output(D1,GPIO.LOW)
    GPIO.output(D2,GPIO.HIGH)
    GPIO.output(D3,GPIO.HIGH)
    GPIO.output(D4,GPIO.LOW)

def turnRight():
    GPIO.output(D1,GPIO.LOW) 
    GPIO.output(D2,GPIO.LOW)
    GPIO.output(D3,GPIO.HIGH)
    GPIO.output(D4,GPIO.HIGH)

def turnLeft():
    GPIO.output(D1,GPIO.HIGH) 
    GPIO.output(D2,GPIO.HIGH)
    GPIO.output(D3,GPIO.LOW)
    GPIO.output(D4,GPIO.LOW)

while 1:
    peripheralLoop()
    turnRight()
    time.sleep(2)
    turnUp()
    time.sleep(1)

    pass

    if _name_=='_main_':
        main()

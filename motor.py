import RPi.GPIO as GPIO
import time
import datetime
import os

led_pin = 17

def set_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.LOW)
    print("GPIOs set-up")
    
def clean_gpio():
    print('Mode Check Before Cleanup: ' + str(type(GPIO.getmode())))
    if isinstance(GPIO.getmode(), int):
        GPIO.cleanup()
    print('Mode Check After Cleanup: ' + str(GPIO.getmode()))

def motor(flag):
    # check if GPIO.setmode(GPIO.BCM) = 11
    if not isinstance(GPIO.getmode(), int):
        set_gpio()
    global led_pin
    if flag == "on":
        GPIO.output(led_pin, GPIO.HIGH)
        print('LED on')
    else:
        GPIO.output(led_pin, GPIO.LOW)
        print('LED off')
        clean_gpio()
    
# setup GPIOs for sensor and led
set_gpio()

print("Everything has been setup")





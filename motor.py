import RPi.GPIO as GPIO
import time
import datetime
import os

def set_gpio():
    # set the pins numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    # Select the signal to select ASK/FSK
    GPIO.setup(18, GPIO.OUT)

    # Select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)

    # Disable the modulator by setting CE pin lo
    GPIO.output (22, False)

    # Set the modulator to ASK for On Off Keying 
    # by setting MODSEL pin lo
    GPIO.output (18, False)

    # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output (11, False)
    GPIO.output (15, False)
    GPIO.output (16, False)
    GPIO.output (13, False)
    print("GPIOs set-up")
    
def clean_gpio():
    print('Mode Check Before Cleanup: ' + str(type(GPIO.getmode())))
    if isinstance(GPIO.getmode(), int):
        GPIO.cleanup()
    print('Mode Check After Cleanup: ' + str(GPIO.getmode()))
    
def controll_socket(flag):
    if flag == "on":
        print("sending code 1110 socket 2 on")
        GPIO.output (11, False)
        GPIO.output (15, True)
        GPIO.output (16, True)
        GPIO.output (13, True)
        # let it settle, encoder requires this
        time.sleep(0.1)
        # Enable the modulator
        GPIO.output (22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output (22, False)
    else:
        print("sending code 0110 socket 2 off")
        GPIO.output (11, False)
        GPIO.output (15, True)
        GPIO.output (16, True)
        GPIO.output (13, False)
        # let it settle, encoder requires this
        time.sleep(0.1)
        # Enable the modulator
        GPIO.output (22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output (22, False)

def motor(flag):
    # check if GPIO.setmode(GPIO.BOARD) = 10
    if not isinstance(GPIO.getmode(), int):
        print(str(GPIO.getmode()))
        set_gpio()
    if flag == "on":
        print(str(GPIO.getmode()))
        controll_socket("on")
        print('motor on')
    else:
        controll_socket("off")
        print('motor off')
        clean_gpio()
    
# setup GPIOs for sensor and led
set_gpio()

print("Everything has been setup")

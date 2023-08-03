#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

PIN_TRIGGER = 11
PIN_ECHO = 7
PIN_LED = 12
PIN_LED2 = 32

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
def measure():
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    print ("Waiting for sensor to settle")

    time.sleep(2)
    print ("Calculating distance")

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print("Distance", distance, "cm")
    GPIO.setup(PIN_LED, GPIO.OUT)
    GPIO.setup(PIN_LED2 , GPIO.OUT)
    if distance < 15:
            print ("LED1 ON")
            GPIO.output(PIN_LED, GPIO.HIGH)
            print ("LED2 OFF")
            GPIO.output(PIN_LED2, GPIO.LOW)
            
            while distance < 15:
                    time.sleep(0.1)
                    measure()
    elif ((distance > 15) and (distance < 25)) :
            GPIO.output(PIN_LED2, GPIO.HIGH)
            print ("LED1 OFF")
            GPIO.output(PIN_LED, GPIO.LOW)
            while ((distance > 15) and (distance < 25)):
                    time.sleep(0.1)
                    measure()
    else:
    
            print ("LED OFF")
            GPIO.output(PIN_LED2, GPIO.LOW)
            GPIO.output(PIN_LED, GPIO.LOW)

            
            
            
while True:
    measure()

GPIO.cleanup()
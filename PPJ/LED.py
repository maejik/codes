#!/usr/bin/env python3
# coding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(11, GPIO.OUT)       # rain
GPIO.output(11, GPIO.HIGH)     # rain
GPIO.setup(13, GPIO.OUT)       # cloud
GPIO.output(13, GPIO.HIGH)     # cloud
GPIO.setup(15, GPIO.OUT)       # clear
GPIO.output(15, GPIO.HIGH)     # clear

for i in range(1,10):
        
        print ('...led on')
        GPIO.output(11,13,15, GPIO.LOW)  # led on
        time.sleep(0.5)
        
        print ('led off...')
        GPIO.output(11,13,15, GPIO.HIGH) # led off
        time.sleep(0.5)

GPIO.output(15, GPIO.HIGH)     # led off
GPIO.cleanup()                 # Release resource
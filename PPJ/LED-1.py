  GNU nano 3.2                                     LED.py

#!/usr/bin/env python3
# coding: utf-8

import RPi.GPIO as GPIO
import time

Gr_LED =11
B_LED =15
Y_LED =18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(Gr_LED, GPIO.OUT)
GPIO.setup(B_LED, GPIO.OUT)
GPIO.setup(Y_LED, GPIO.OUT)

GPIO.output(Gr_LED, GPIO.HIGH)
GPIO.output(B_LED, GPIO.HIGH)
GPIO.output(Y_LED, GPIO.HIGH)
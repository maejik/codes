#!/usr/bin/env python3
# coding: utf-8

import RPi.GPIO as GPIO
import time

Gr_LED =11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(Gr_LED, GPIO.OUT)
GPIO.output(Gr_LED, GPIO.LOW)
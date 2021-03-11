#!/usr/bin/env python3
# coding: utf-8

import RPi.GPIO as GPIO
import time

B_LED =15
Y_LED =18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(B_LED, GPIO.OUT)
GPIO.setup(Y_LED, GPIO.OUT)

GPIO.output(B_LED, GPIO.HIGH)
GPIO.output(Y_LED, GPIO.HIGH)


import json
import datetime
import os
import requests
import sys

tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
dt = datetime.datetime.now(tokyo_tz)

city = "Mitaka-shi"
key = 'dd2d71e62067880d0c1a39d7297a9b6f'
url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q=' + city + '&APPID=' + key

print(url)
response = requests.get(url)

print("---")
data = response.json()
jsonText = json.dumps(data, indent=4)
print(jsonText)
print("---")
data = json.loads(response.text)
print(city)
print(dt)
print("weather ID:", data["weather"][0]["id"])
print("weather:", data["weather"][0]["main"])
print("temp:", data["main"]["temp"])
print("temp_min:", data["main"]["temp_min"])
print("temp_max:", data["main"]["temp_max"])

wid = (data["weather"][0]["id"])
weather = (data["weather"][0]["main"])
temp_min = (data["main"]["temp_min"])

if wid < 800:
 GPIO.output(B_LED, GPIO.LOW)

if temp_min >= 5.00:
  GPIO.output(Y_LED, GPIO.LOW)

def main():
    # set LINE Notify Token
    access_token = 'DBs4IYMfdbgUOHdcEyQ4mjs4ZYO8zAccyn7xfY9aJg1'
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }
    payload = {
        'message':(weather)
    }

    # request Notify
    response = requests.post(url, headers=headers, params=payload)
    res = json.loads(response.text)
    print(res)

    return True

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# coding: utf-8

import json
import datetime
import os
import requests
import sys

API_KEY = 'dd2d71e62067880d0c1a39d7297a9b6f'
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

city_name = "Mitaka-shi"
url = api.format(city = city_name, key = API_KEY)
response = requests.get(url)
data = json.loads(response.text)
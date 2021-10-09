import requests
import json
import datetime
import time
from types import SimpleNamespace

API_UBIDOTS = "http://things.ubidots.com/api/v1.6/devices/{device_label}/{variable_label}/values/"
TOKEN_UBIDOTS = "BBFF-7uyH9eVXScLcZ0inSIGLJq0WkXcQn2"

def _requestData(url, url_pram):
    response = requests.get(url,url_param)
    return  json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))

def _processData(data):
    print(data.value)
    print(data.timestamp)

with open('./estaciones.json', 'r') as file:
    config = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))

now = datetime.datetime.now()
#print(round(time.time() * 1000))
now = round(time.time() * 1000)
#tn = datetime.datetime.timestamp(now)
#yday = datetime.datetime.now() - datetime.timedelta(days=1)
#tyd = datetime.datetime.timestamp(yday)
for cf in config:
    url_param = {'token':cf.token,'start':(now-86400000), 'end':now}
    for param in cf.params:
        url = API_UBIDOTS.format(device_label=cf.device_label,variable_label= param.variable_label)
        responseData = _requestData(url, url_param)
        for item in responseData.results:
            _processData(item)
        


#
'''for cf in config:
    url_param = {'token':cf["token"],'start':(now-86400000), 'end':now}
    print(url_param)
    for param in cf["params"]:
        url = API_UBIDOTS.format(device_label=cf["device_label"],variable_label= param["variable_label"])
        print(url)
        response = requests.get(url,url_param)
        data = response.json()
        print(data)
        for item in data["results"]:
            print("estacion ", cf["id"])
            print("parametro ",param["id"])
            print(item["value"])
            print(item["timestamp"])
'''
##for cf in config:
#    print(cf)

"""
url = API_UBIDOTS.format(device_label=cf["device_label"],variable_label= param["variable_label"])
        print(url)
        response = requests.get(url,params)

        data = response.json()
#clear

        for item in data["results"]:
            print(item["value"])
            print(item["timestamp"])
"""
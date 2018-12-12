#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-
import json
import time
import random
import paho.mqtt.client as mqtt

ip = '161.67.33.218' #professor's server
def callback(client, userdata, message):
    token = message.payload.decode()
    data = {
        'token': token,
        'fullname': 'Juan Perea',
        'identifier': '00000000A-Z',
        'grade': 'PASS',
    }
    publisher = mqtt.Client()
    publisher.connect(ip)
    while 1:
        publisher.publish('students', json.dumps(data))
        time.sleep(1)

subscriber = mqtt.Client()
subscriber.on_message = callback
subscriber.connect(ip)
subscriber.subscribe('tokens')
subscriber.loop_forever()

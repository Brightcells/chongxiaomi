# -*- coding: utf-8 -*-

from django.test import Client, TestCase

from data.models import BatteryInfo

import json
import Cookie


class BatteryInfoTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_batteryinfo(self):
        data = {
            'batteryinfo': [
                {
                    "token": "An8neZnc5N1WoXmS0DNCaEWuPWcZ_VFj6tbExOcU1bRG",
                    "logtime": "20140629 15:40:21",
                    "level": "81",
                    "voltage": "3898",
                    "temperature": "310",
                    "status": "2",
                    "health": "2",
                    "isProtected": "false",
                },
                {
                    "token": "An8neZnc5N1WoXmS0DNCaEWuPWcZ_VFj6tbExOcU1bRG",
                    "logtime": "20140629 15:40:21",
                    "level": "81",
                    "voltage": "3898",
                    "temperature": "310",
                    "status": "2",
                    "health": "2",
                    "isProtected": "false",
                },
            ]
        }
        response = self.client.post('/data/batteryinfo', data=data)
        print BatteryInfo.objects.all().values()
        print
        print response.content
        self.assertEqual(True, json.loads(response.content)['status'])

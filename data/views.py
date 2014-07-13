# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from CodeConvert import CodeConvert

from data.models import BatteryInfo
from data.forms import BatteryInfoModelForm
from utils.json_utils import JsonHttpResponse

import ast
import json
import requests

from datetime import datetime


def change_list_2_utf8(obj):
    return [dict((CodeConvert.Convert2Utf8(k), CodeConvert.Convert2Utf8(v)) for k, v in dic.items()) for dic in obj]


def change_dict_2_utf8(obj):
    return dict((CodeConvert.Convert2Utf8(k), CodeConvert.Convert2Utf8(v)) for k, v in obj.items())


@csrf_exempt
def batteryinfo(request):
    try:
        binfo = json.loads(request.body).get('batteryinfo', '')
    except:
        binfo = request.POST.getlist('batteryinfo', '')

    status = True

    try:
        for info_dict in binfo:
            info_dict = ast.literal_eval(info_dict) if isinstance(info_dict, unicode) else info_dict
            info_dict['logtime'] = datetime.strptime(info_dict['logtime'], '%Y%m%d %H:%M:%S')
            form = BatteryInfoModelForm(info_dict)
            if form.is_valid():
                form.save()
            else:
                status = False
    except:
        status = False

    return JsonHttpResponse({'status': status})

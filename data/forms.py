# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import Textarea, ClearableFileInput, URLInput, Select
from django.utils.translation import ugettext_lazy as _

from data.models import BatteryInfo


class BatteryInfoModelForm(ModelForm):
    class Meta:
        model = BatteryInfo

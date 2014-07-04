# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext

from chongxiaomi.basemodels import CreateUpdateMixin


class BatteryInfo(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'用户唯一标示码')
    logtime = models.DateTimeField(_(u'logtime'), blank=True, null=True, help_text=u'当前日志的时间，是一个"yyyyMMdd HH:mm:ss"格式的字符串')
    level = models.IntegerField(_(u'level'), default=0, help_text=u'电池电量信息，int类型，取值范围[0,100]，表示电量占总电量的比例')
    voltage = models.IntegerField(_(u'voltage'), default=0, help_text=u'电池电压信息，int类型，单位是mV')
    temperature = models.IntegerField(_(u'temperature'), default=0, help_text=u'电池温度信息，int类型，单位是0.1℃')
    status = models.IntegerField(_(u'status'), default=0, help_text=u'电池充电状态码，int类型，取固定的几个值: {1,2,3,4,5}')
    health = models.IntegerField(_(u'health'), default=0, help_text=u'电池健康状态码，int类型，取固定的几个值: {1,2,3,4,5,6}')
    isProtected = models.BooleanField(_(u'isProtected'), default=False, help_text=u'标志位，当前状态是否是自动断电')

    class Meta:
        verbose_name = _(u'batteryinfo')
        verbose_name_plural = _(u'batteryinfo')

    def __unicode__(self):
        return unicode(self.token)

    def _data(self):
        return {
            'pk': self.pk,
            'token': self.token,
            'logtime': self.logtime,
            'level': self.level,
            'voltage': self.voltage,
            'temperature': self.temperature,
            'status': self.status,
            'health': self.health,
            'isProtected': self.isProtected,
        }

    data = property(_data)

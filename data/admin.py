from django.contrib import admin

from data.models import BatteryInfo


class BatteryInfoAdmin(admin.ModelAdmin):
    list_display = ('token', 'logtime', 'level', 'voltage', 'temperature', 'status', 'health', 'isProtected', 'create_at', 'modify_at')


admin.site.register(BatteryInfo, BatteryInfoAdmin)

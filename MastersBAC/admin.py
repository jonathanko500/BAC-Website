# admin.py
from django.contrib import admin
from .models import ScheduleSwim, SchedulePolo

admin.site.register(ScheduleSwim)
admin.site.register(SchedulePolo)

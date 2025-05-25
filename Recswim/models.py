# models.py is used to create the database tables for the Lapswim app
from django.db import models


class Schedule(models.Model):

    urgent = models.TextField(blank=True, null=True)

    info = models.TextField(blank=True, null=True)

    weekdays = models.CharField(max_length=255, blank=True, null=True)
    weekdays_timeframe = models.CharField(
        max_length=255, blank=True, null=True)

    weekends = models.CharField(max_length=255, blank=True, null=True)
    weekends_timeframe = models.CharField(
        max_length=255, blank=True, null=True)
    daily_fee = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

    registration_info = models.TextField(blank=True, null=True)

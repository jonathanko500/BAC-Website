# models.py is used to create the database tables for the Lapswim app
from django.db import models


class Schedule(models.Model):
    WEEKDAY_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    ]

    urgent = models.TextField(blank=True, null=True)

    weekdays_morning = models.CharField(max_length=255, blank=True, null=True)
    weekdays_afternoon = models.CharField(
        max_length=255, blank=True, null=True)
    weekdays_evening = models.CharField(max_length=255, blank=True, null=True)

    saturday = models.CharField(max_length=255, blank=True, null=True)
    sunday = models.CharField(max_length=255, blank=True, null=True)

    shortCourse_occur = models.CharField(max_length=255, blank=True, null=True)
    longCourse_occur = models.CharField(max_length=255, blank=True, null=True)

    info = models.TextField(blank=True, null=True)

    daily_fee = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    monthly_fee = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    quarterly_fee = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

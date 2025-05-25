# models.py is used to create the database tables for the Lapswim app
from django.db import models


class ScheduleSwim(models.Model):
    urgent = models.TextField(blank=True, null=True)

    philosophy = models.TextField(blank=True, null=True)

    # timeframe of practice
    weekdays_morning = models.CharField(max_length=255, blank=True, null=True)
    weekdays_afternoon = models.CharField(
        max_length=255, blank=True, null=True)

    weekends = models.CharField(max_length=255, blank=True, null=True)

    # when practices are held
    # SC_morning_practices = models.CharField(
    #     max_length=255, blank=True, null=True, verbose_name="Short Course Morning Practice")
    # SC_afternoon_practices = models.CharField(
    #     max_length=255, blank=True, null=True, verbose_name="Short Course Afternoon Practice")
    # SC_weekend_practices = models.CharField(
    #     max_length=255, blank=True, null=True, verbose_name="Short Course Weekend Practice")

    # LC_morning_pracitces = models.CharField(
    #     max_length=255, blank=True, null=True, verbose_name="Long Course Morning Practice")
    # LC_weekend_pracitces = models.CharField(
    #     max_length=255, blank=True, null=True, verbose_name="Long Course Weekend Practice")

    # money stuff
    registration = models.TextField(blank=True, null=True)

    ticket_pass = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    monthly_fee = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    daily_fee = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

    # newsletter
    newsletterDate = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Date of Newsletter Update")
    newsletterLink = models.URLField(
        blank=True, null=True, verbose_name="Newsletter Link")

    # special events
    specEvent_display = models.BooleanField(
        default=False, help_text="Check this to display Special Events on the website")
    specEvent_title = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Special Event Title")
    specEvent_desc = models.TextField(
        blank=True, null=True, verbose_name="Special Event Description")
    specEVent_registration_link = models.URLField(
        blank=True, null=True, verbose_name="Special Event Link")
    specEvent_button_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Name of Button Link")



class SchedulePolo(models.Model):
    urgent = models.TextField(blank=True, null=True)
    philosophy = models.TextField(blank=True, null=True)
    schedule_notes = models.TextField(blank=True, null=True)

    weekday = models.CharField(max_length=255, blank=True, null=True)
    weekdays_timeframe = models.CharField(
        max_length=255, blank=True, null=True)

    weekends = models.CharField(max_length=255, blank=True, null=True)
    weekends_timeframe = models.CharField(
        max_length=255, blank=True, null=True)

    location = models.TextField(blank=True, null=True)

    practiceNotes_one = models.TextField(blank=True, null=True)
    practiceNotes_two = models.TextField(blank=True, null=True)
    practiceNotes_three = models.TextField(blank=True, null=True)
    practiceNotes_four = models.TextField(blank=True, null=True)

    registration = models.TextField(blank=True, null=True)

    gold_fee = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Gold Team Fee", blank=True, null=True)
    blue_fee = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Blue Team Fee", blank=True, null=True)
    ticket_fee = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="10-pack Fee", blank=True, null=True)
    daily_fee = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Drop-in Fee", blank=True, null=True)

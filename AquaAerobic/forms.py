from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['urgent', 'days', 'timeframe', 'info', 'daily_fee']

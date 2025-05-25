from django import forms
from .models import Holiday

class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = '__all__'
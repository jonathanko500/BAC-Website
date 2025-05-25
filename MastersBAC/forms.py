from django import forms
from .models import ScheduleSwim, SchedulePolo


class ScheduleSwimForm(forms.ModelForm):
    class Meta:
        model = ScheduleSwim
        fields = '__all__'  # This includes all fields from your model in the form

    # You can add additional customization or validation here if needed


class SchedulePoloForm(forms.ModelForm):
    class Meta:
        model = SchedulePolo
        fields = '__all__'  # This includes all fields from your model in the form

    # You can add additional customization or validation here if needed

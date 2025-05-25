
from django import forms
from .models import AGswimPage, AGpoloPage
# from .models import GroupDetailSchedule


class AGswimPageForm(forms.ModelForm):
    class Meta:
        model = AGswimPage
        fields = '__all__'  # This includes all fields from your model in the form


class AGpoloPageForm(forms.ModelForm):
    class Meta:
        model = AGpoloPage
        fields = '__all__'  # This includes all fields from your model in the form
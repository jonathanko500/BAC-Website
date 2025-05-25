from django import forms
from .models import homePage

class homePageForm(forms.ModelForm):
    class Meta:
        model = homePage
        fields = '__all__'  # This includes all fields from your model in the form

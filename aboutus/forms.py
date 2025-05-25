from django import forms
from .models import aboutusEdit, jobDesc


class aboutusEditForm(forms.ModelForm):
    class Meta:
        model = aboutusEdit
        fields = '__all__'  # This includes all fields from your model in the form




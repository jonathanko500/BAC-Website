from django import forms
from .models import Program, Session, WeekendSession, PageInfo

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'

class WeekendSessionForm(forms.ModelForm):
    class Meta:
        model = WeekendSession
        fields = '__all__'

class PageInfoForm(forms.ModelForm):
    class Meta:
        model = PageInfo
        fields = '__all__'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data['email']
        
        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        
        if not email.endswith('@burlingameaquatics.com'):
            raise forms.ValidationError("Only email addresses from @burlingameaquatics.com are allowed.")
        
        return email
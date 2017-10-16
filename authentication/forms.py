from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class CustomUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError("This email address is already in use")
        return self.cleaned_data["email"]


from django import forms
from django.core.exceptions import ValidationError 
from django.contrib.auth.models import User

def Validate_Phone(value):
    if len(str(value)) != 10:
        raise ValidationError("Enter the correct phone number")

def Validate_Username(username):
    if User.objects.filter(username=username).exists():
        raise ValidationError("Username already taken")


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "Username","required":True, "class": "form-control"}),error_messages={"required":"Username missing"}, validators=[Validate_Username])

    phone = forms.IntegerField(label="Phone Number", widget=forms.NumberInput(attrs={"placeholder": "Phone Number","required":True, "class": "form-control"}),error_messages={"required":"Phone number missing"}, validators=[Validate_Phone])

    fname = forms.CharField(max_length=20, label="First Name", widget=forms.TextInput(attrs={"placeholder": "First Name","required":True, "class": "form-control"}),error_messages={"required":"First name missing"})

    lname = forms.CharField(max_length=20, label="Last Name", widget=forms.TextInput(attrs={"placeholder": "Last Name","required":True, "class": "form-control"}),error_messages={"required":"Last name missing"})

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Password","required":True, "class": "form-control"}),error_messages={"required":"Password field missing"})

    password2 = forms.CharField(label="Re-Enter Password", widget=forms.PasswordInput(attrs={"placeholder": "Password","required":True, "class": "form-control"}),error_messages={"required":"Password field missing"})

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get("password1")
        pass2 = cleaned_data.get("password2")

        if(pass1 != pass2):
            raise ValidationError("Password not matching")
        
            
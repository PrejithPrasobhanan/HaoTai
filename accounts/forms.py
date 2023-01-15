from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    enter_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =( 'username','email')

    def clean(self):
        cleaned_data = super().clean()
        enter_password = self.cleaned_data.get("enter_password")
        confirm_password = self.cleaned_data.get("confirm_password")
        
        if enter_password != confirm_password:
            print("hello----")
            print(enter_password,confirm_password)
            raise forms.ValidationError(
                "enter_password and confirm_password does not match"
            )


    
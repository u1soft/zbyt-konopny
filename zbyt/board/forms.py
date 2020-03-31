from django import forms
from django.forms import ClearableFileInput

from .models import Advert, AdvertFile
from .validators import validate_username


class LoginUser(forms.Form):
    username = forms.CharField(max_length=20, label="Nazwa użytkoniwka")
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterUser(forms.Form):
    first_name = forms.CharField(max_length=200, label="Imię")
    last_name = forms.CharField(max_length=200, label="Nazwisko")
    email = forms.CharField(widget=forms.EmailInput, label="Adres Email")
    username = forms.CharField(max_length=20, label="Nazwa użytkoniwka", validators=[validate_username])
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(help_text='Powtórz hasło', widget=forms.PasswordInput)


class AddAdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        exclude = ['creator', 'pub_date']


class AddAdvertFileForm(forms.ModelForm):
    class Meta:
        model = AdvertFile
        exclude = ['advert']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True})
        }

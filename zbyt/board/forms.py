from django import forms
from .choices import Choices
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


class AddAdvertForm(forms.Form):
    title = forms.CharField(max_length=200, label="Tytuł")
    body = forms.CharField(widget=forms.Textarea, label="Opis")
    type = forms.ChoiceField(choices=Choices.types, label="Typ ogłoszenia", initial="sell")
    category = forms.ChoiceField(choices=Choices.categories, label="Kategoria", initial="seed")
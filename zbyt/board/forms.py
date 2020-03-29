from django import forms
from .choices import Choices


class AddAdvertForm(forms.Form):
    first_name = forms.CharField(max_length=200, label="Imię")
    last_name = forms.CharField(max_length=200, label="Nazwisko")
    email = forms.CharField(max_length=200, label="Adres Email")
    title = forms.CharField(max_length=200, label="Tytuł")
    body = forms.CharField(widget=forms.Textarea, label="Opis")
    type = forms.ChoiceField(choices=Choices.types, label="Typ ogłoszenia", initial="sell")
    category = forms.ChoiceField(choices=Choices.categories, label="Kategoria", initial="seed")


class RegisterUser(forms.Form):
    first_name = forms.CharField(max_length=200, label="Imię")
    last_name = forms.CharField(max_length=200, label="Nazwisko")
    email = forms.CharField(max_length=200, label="Adres Email")
    username = forms.CharField(max_length=20, label="Nazwa użytkoniwka")
    password = forms.CharField(widget=forms.PasswordInput())

from django import forms


class AddAdvertForm(forms.Form):
    first_name = forms.CharField(max_length=200, label="First name")
    last_name = forms.CharField(max_length=200, label="Last name")
    email = forms.CharField(max_length=200, label="Email address")
    title = forms.CharField(max_length=200, label="Advert title")
    body = forms.CharField(max_length=5000, label="Advert body")
    types = [('sell', "Sell"),
             ('buy', "Buy"),
             ('barter', "Exchange")]
    type = forms.ChoiceField(choices=types, label="Advert type", initial="sell")

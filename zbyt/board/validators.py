from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.forms import forms
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


def validate_username(username):
    print("Username validation in progress")
    try:
        username_taken = User.objects.get(username=username)
        if username_taken is not None:
            print("Username taken!")
            raise forms.ValidationError('Nazwa użytkownika jest zajęta!', code='zajęta')
        return username
    except ObjectDoesNotExist:
        return username

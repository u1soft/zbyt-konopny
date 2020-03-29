from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


class Advert(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=5000)
    types = [('sell', "Sell"),
             ('buy', "Buy"),
             ('barter', "Exchange")]
    type = models.CharField(max_length=6,
                            choices=types,
                            default='sell')
    pub_date = models.DateTimeField('date published')
    creator = User

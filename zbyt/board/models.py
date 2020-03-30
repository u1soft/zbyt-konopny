from django.db import models
from .choices import Choices


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=30)


class Advert(User):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=5000)

    type = models.CharField(max_length=6,
                            choices=Choices.types,
                            default='sell')
    category = models.CharField(max_length=6,
                                choices=Choices.categories,
                                default='seed')
    pub_date = models.DateTimeField('date published')

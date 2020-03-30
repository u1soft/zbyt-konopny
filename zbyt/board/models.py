from django.db import models
from .choices import Choices
from django.contrib.auth.models import User


class Advert(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=5000)

    type = models.CharField(max_length=6,
                            choices=Choices.types,
                            default='sell')
    category = models.CharField(max_length=6,
                                choices=Choices.categories,
                                default='seed')
    pub_date = models.DateTimeField('date published')
    creator = models.ForeignKey(User, related_name="created_by",
                                on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.title

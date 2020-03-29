from django.db import models


class Advert(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')
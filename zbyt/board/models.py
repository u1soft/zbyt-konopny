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


def user_dir_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class AdvertFile(models.Model):
    file = models.ImageField(upload_to=user_dir_path,
                             blank=True,
                             null=True,
                             help_text="Jeden lub więcej plików")
    advert = models.ForeignKey(Advert,
                               on_delete=models.CASCADE,
                               related_name='files')

    objects = models.Manager()

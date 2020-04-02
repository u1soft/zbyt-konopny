from ..models import AdvertFile, Advert
from django import template

register = template.Library()


@register.filter
def get_first_photo(advert_pk):
    url = "/static/no_picture.jpg"
    ad = AdvertFile.objects.filter(advert=advert_pk).first()
    if ad is not None:
        url = '/user_' + Advert.objects.filter(id=advert_pk).get().creator.username
        url = ad.file.url[0:7] + url + ad.file.url[7:]
        print("Debug urls...")
        print(url)
    return url

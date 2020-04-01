from ..models import AdvertFile
from django import template

register = template.Library()


@register.filter
def get_first_photo(advert_pk):
    url = None
    ad = AdvertFile.objects.filter(advert=advert_pk).first()
    if ad is not None:
        url = ad.file.url
    return url

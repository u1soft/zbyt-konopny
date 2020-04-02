from ..models import AdvertFile, Advert
from django import template
from sorl.thumbnail import get_thumbnail

register = template.Library()


@register.filter
def get_first_photo(advert_pk):
    img = "no_picture.jpg"
    no_pic = get_thumbnail(img, '150x150', crop='center', quality=99)
    ad = AdvertFile.objects.filter(advert=advert_pk).first()
    if ad is not None:
        print(ad.file.path)
        im = get_thumbnail(ad.file.path, '150x150', crop='center', quality=99)
        return im.url
    else:
        return no_pic.url

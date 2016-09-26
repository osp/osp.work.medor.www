# -*- coding: utf-8 -*-

from django import forms
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer


class CustomOrderMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        if obj.image:
            thumbnailer = get_thumbnailer(obj.image)
            thumbnail_options = {'crop': False}
            thumbnail_options.update({'size': (300, 400)})
            thumb = thumbnailer.get_thumbnail(thumbnail_options)
            return mark_safe(u'<img src="{}"><span>{}. {} €</span>'.format(thumb.url, obj.name, obj.price))
        else:
            return mark_safe(u'{}. {} €'.format(obj.name, obj.price))

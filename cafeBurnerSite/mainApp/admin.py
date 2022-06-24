from django.contrib import admin
from django.utils.html import format_html


# Register your models here.
from .models import *

# admin.site.register(Flyer_Image)
# admin.site.register(Flyer)
admin.site.register(Reminder)

@admin.register(Flyer) 
class FlyerAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        if obj.Flyer_image.Flyer_image:
            return format_html('<img src="/media/{}" "width="99" height="99"/>'.format(obj.Flyer_image.Flyer_image))
        if obj.Flyer_image.Url:
            return format_html('<img src="{}" "width="99" height="99"/>'.format(obj.Flyer_image.Url))


    image_tag.short_description = 'Image'
    list_display = ['Event_date', 'image_tag',]





@admin.register(Flyer_Image) 
class Flyer_ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        if obj.Flyer_image:
            return format_html('<img src="/media/{}" "width="99" height="99"/>'.format(obj.Flyer_image))
        if obj.Url:
            return format_html('<img src="{}" "width="99" height="99"/>'.format(obj.Url))

    image_tag.short_description = 'Image'
    list_display = ['image_tag',]
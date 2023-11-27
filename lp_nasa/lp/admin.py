from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from lp.models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'display_image', 'pub_date')

    def display_image(self, obj):
        return format_html(
            '<img src="{}" width="100" height="100" />',
            obj.image.url
        ) if obj.image else ''

    display_image.short_description = 'image'

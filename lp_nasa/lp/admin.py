from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from lp.models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image', 'pub_date')

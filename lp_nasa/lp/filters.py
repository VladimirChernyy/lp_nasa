import django_filters

from lp.models import SliderImage


class SliderFilter(django_filters.FilterSet):
    class Meta:
        model = SliderImage
        fields = {
            'title': ['exact', 'contains'],
        }

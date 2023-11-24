from django.views.generic import ListView
from django.shortcuts import get_list_or_404

from lp.filters import SliderFilter
from lp.models import SliderImage


class TopPage(ListView):
    # model = SliderImage
    template_name = 'lp/index.html'

    def get_queryset(self):
        return SliderFilter(
            self.request.GET,
            queryset=SliderImage.objects.all()
        )

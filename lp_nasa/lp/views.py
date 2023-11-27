from django.views.generic import ListView

from lp.models import SliderImage


class TopPage(ListView):
    model = SliderImage
    template_name = 'lp/index.html'

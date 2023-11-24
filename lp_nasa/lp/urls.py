from django.urls import path

from lp.views import TopPage

app_name = 'lp'

urlpatterns = [
    path('', TopPage.as_view(), name='top_page'),
]

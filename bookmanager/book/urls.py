from django.conf.urls import url

from book.views import *


urlpatterns = [
    url(r'^index/$', index),
    url(r'^$', index),
]
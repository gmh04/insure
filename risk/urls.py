from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<risk>(\w*))$', views.api, name='index'),
]

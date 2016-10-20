from django.conf.urls import url

from . import views

app_name = 'urmom'


urlpatterns = [
    # /urmom/
    url(r'^$', views.index, name='index'),


    # /urmom/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
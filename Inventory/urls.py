from django.conf.urls import url

from . import views


app_name = 'Inventory'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'additem/', views.additem, name='additem'),
    url(r'^password/(?P<password>.+)/$',views.login,name='login'),


    url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<item_id>[0-9]+)/removeitem', views.removeitem, name='removeitem'),


]
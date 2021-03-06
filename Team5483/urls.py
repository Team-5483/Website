"""Team5483 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Home.urls')),

    url(r'^inventory/', include('Inventory.urls')),
    url(r'^Inventory/', include('Inventory.urls')),

    url(r'^inventory/login', include('Login.urls')),
    url(r'^Inventory/login', include('Login.urls')),

    url(r'^Inventory/import', include('ExcelParser.urls')),
    url(r'^inventory/import', include('ExcelParser.urls')),

    url(r'^Inventory/export', include('Export.urls')),
    url(r'^inventory/export', include('Export.urls')),

]

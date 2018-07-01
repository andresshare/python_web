"""root_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from app_login import views
from app_contacto import views





urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^formpage/', views.form_name_view, name = 'form_name_view'),
    url(r'^contacto/', views.contacto, name = "contacto"),
    url(r'^formbd/', include('app_contacto.urls')),
    url(r'^login/', include('app_login.urls')),
    url(r'^basicapp/', include('app_contacto.urls')),
    url(r'^app_login/', include('app_login.urls')),
    url(r'^admin/', admin.site.urls),
]

from django.conf.urls import url
from app_contacto import views


urlpatterns = [
    #url(r'^$', views.contacto, name="contacto"),
    url(r'^$', views.users, name="users")
]





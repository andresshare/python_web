from django.conf.urls import url
from app_login import views


urlpatterns = [
    url(r'^$', views.login, name="login")
]

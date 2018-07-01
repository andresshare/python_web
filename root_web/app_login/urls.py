from django.conf.urls import url
from app_login import views


urlpatterns = [
    url(r'^$', views.login, name="login")

]

#TEMPLATE URLS
app_name = 'app_login'

urlpatterns = [
    url(r'^register/$', views.register, name="register")
]

from django.conf.urls import url
from app_contacto import views


urlpatterns = [
    url(r'^$', views.contacto, name="contacto"),
    url(r'^$', views.users, name="users")
]

#TEMPLATE_TAGGING
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]






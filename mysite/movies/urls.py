from django.conf.urls import url, include
from movies import views

urlpatterns = [
   
    url(r'^test/$', views.show, name='test'),
]

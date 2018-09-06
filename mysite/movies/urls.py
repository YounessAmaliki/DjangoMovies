from django.conf.urls import url, include
from movies import views

urlpatterns = [
   
    url(r'^test/$', views.show, name='test'),
    url(r'^', views.actors, name='actors'),
    url(r'^(?P<movie>[a-Z]+)/actors/$', views.results, name='results'),
]

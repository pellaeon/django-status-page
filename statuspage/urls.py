from django.conf.urls import patterns, url
from statuspage import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^monitor/(\d+)/D$', views.set_down, name='set_down'),
        url(r'^monitor/(\d+)/U$', views.set_up, name='set_up'),
        )

from django.conf.urls import patterns, url
from statuspage import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        )

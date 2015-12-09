from django.conf.urls import patterns, url
from statuspage import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
        url(r'^monitors/$', views.MonitorList.as_view()),
        url(r'^monitors/(?P<pk>.+)/$', views.MonitorDetail.as_view()),
        ]

urlpatterns = format_suffix_patterns(urlpatterns)

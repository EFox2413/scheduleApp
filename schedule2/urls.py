from django.conf.urls import patterns, url

from schedule2 import views

urlpatterns = patterns('',
        # ex: /schedules/
        url(r'^$', views.index, name='index'),
        # ex: /schedules/aggreg
        url(r'aggregate/$', views.aggregate, name='aggregate'),
        )

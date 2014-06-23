from django.conf.urls import patterns, url

from schedule2 import views

urlpatterns = patterns('',
        # ex: /schedules/
        url(r'^$', views.index, name='index'),
        # ex: /schedules/aggreg
        url(r'aggregate/$', views.aggregate, name='aggregate'),
        # ex: /schedules/makesublist
        url(r'^makeSubList/$', views.makeSubList, name='makeSubList'),
        # ex: /schedules/testpost
        url(r'^testPost/$', views.testPost, name='testPost'),
        )

from django.conf.urls import patterns, url

from schedule2 import views

urlpatterns = patterns('',
        # ex: /schedules/
        url(r'^$', views.index, name='index'),
        # ex: /schedules/overview
        url(r'overview/$', views.overview, name='overview'),
        # ex: /schedules/makesublist
        url(r'^makeSubList/$', views.makeSubList, name='makeSubList'),
        # ex: /schedules/testpost
        url(r'^testPost/$', views.testPost, name='testPost'),
        # ex: /schedules/submit
        url(r'^submit/$', views.submit, name='submit'),
        # ex: /schedules/overview/data
        url(r'overview/data/$', views.overviewGetData, name='data'),
        )

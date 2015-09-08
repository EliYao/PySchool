from django.conf.urls import patterns, url
from school import views 

urlpatterns = patterns('',
            url(r'^$', views.login, name='login'),
            url(r'^signup/$', views.signup, name='signup'),
            url(r'^index/$', views.index, name='index'),
            )
			
#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from school import views 
urlpatterns = patterns('',
            url(r'^$', views.user_login, name='login'),
            url(r'^signup/$', views.signup, name='signup'),
            url(r'^index/$', views.index, name='index'),
            url(r'^addCourse/$', views.addCourse, name='addCourse'),
            url(r'^addFolder/$', views.addFolder, name='addFolder'),
            url(r'^profileCenter/$', views.profileCenter, name='profileCenter'),
            url(r'^profileFolder/$', views.profileFolder, name='profileFolder'),
            url(r'^profileFolderDetails/$', views.profileFolderDetails, name='profileFolderDetails'),
            url(r'^createLesson/$', views.createLesson, name='createLesson'),
            url(r'^createLessonDefine/$', views.createLessonDefine, name='createLessonDefine'),
            url(r'^createLessonVideo/$', views.createLessonVideo, name='createLessonVideo'),
            url(r'^createLessonText/$', views.createLessonText, name='createLessonText'),
            url(r'^lessonDetails/$', views.lessonDetails, name='lessonDetails'), 
            url(r'^lessonStudy/$', views.lessonStudy, name='lessonStudy'),
            url(r'^logout/$', views.user_logout, name='logout'), 
            url(r'^login/$', views.user_login), 
            url(r'^searchResults/$', views.searchResults, name='searchResults'), 
            url(r'^searchResults_c/$', views.searchResults_c, name='searchResults_c'),
            )
			
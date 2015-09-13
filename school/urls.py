from django.conf.urls import patterns, url
from school import views 

urlpatterns = patterns('',
            url(r'^$', views.login, name='login'),
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
            )
			
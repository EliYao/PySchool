from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

        
urlpatterns = patterns('',
	url(r'^$', include('school.urls')),
    url(r'^school/', include('school.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

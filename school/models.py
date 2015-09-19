#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from django.template.defaultfilters import slugify
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from DjangoUeditor.commands import *
from django.conf import settings

class myEventHander(UEditorEventHandler):
    def on_selectionchange(self):
        return """
            function getButton(btnName){
                var items=%(editor)s.ui.toolbars[0].items;
                for(item in items){
                    if(items[item].name==btnName){
                        return items[item];
                    }
                }
            }
            var btn=getButton("mybtn1");
            var selRanage=id_Description.selection.getRange()
            btn.setDisabled(selRanage.startOffset == selRanage.endOffset);    
    """



#引入 UEditor
class Blog(models.Model):
    Name = models.CharField(u'姓名', max_length=100, blank=True)
    Content = UEditorField(u'内容', width=600, height=300, toolbars="full", imagePath="images/%(basename)s_%(datetime)s.%(extname)s", filePath="images/%(basename)s_%(datetime)s.%(extname)s",upload_settings={"imageMaxSize":1204000}, settings={}, command=None,event_handler=myEventHander(), blank=True)
 
    
    

    
    
#定义用户特性    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    picture = models.ImageField(upload_to='profile_image', blank=True, null=True)

    def __unicode__(self):
		return self.user

    def avatar_image(self):
        return (settings.MEDIA_URL + self.picture.name) if self.picture else None
        
        
#定义课程夹特性        
class Folder(models.Model):
      title = models.CharField(max_length=128)
      describe = models.TextField()
	
      def __unicode__(self):
        return self.title
        
      class Meta:
          ordering = ('title',)
                
#定义课程特性        
class Course(models.Model):
    Folder = models.ManyToManyField(Folder)
    topic = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
	
    def __unicode__(self):
		return self.topic
        
    class Meta:
        ordering = ('topic',)


#定义课时特性        
class Lesson(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=30)
    text = models.TextField()
    video = models.FileField(upload_to='lesson_video', blank=True)
    number = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
        
    class Meta:
        ordering = ('title',)
		

#定义课程评论        
class CourseComments(models.Model):
    course = models.ForeignKey(Course)
    comment = models.CharField(max_length=140)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)	
    
    def __unicode__(self):
		return self.comment
    
	

		

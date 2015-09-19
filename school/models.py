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
from DjangoUeditor.commands import *



def getImagePath(model_instance=None):
    if model_instance is None:
        return "aaa/"
    else:
        return "%s/" % model_instance.Name

def getDescImagePath(model_instance=None):
        return "aaa/"






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

class myBtn(UEditorButtonCommand):
    def onClick(self):
        return u"""
            alert("爽!");
            editor.execCommand(uiName);
        """
    def onExecuteQueryvalueCommand(self):
        return """
            return 1;
        """
    def onExecuteAjaxCommand(self,state):
        if state=="success":
            return u"""
                alert("后面比较爽!"+xhr.responseText);
            """
        if state=="error":
            return u"""
                alert("讨厌，摸哪里去了！"+xhr.responseText);
                """
                
                
class myCombo(UEditorComboCommand):
    def onSelect(self):
        return u"""
            alert("选择了!");
        """
    def get_items(self):
        items=[]
        for i in xrange(10):
            items.append({
                "label":"combo_%s" % i,
                "value":i
            })
        return items



class Blog(models.Model):
    Content = UEditorField('', height=200, width=900, default='请输入你想要的内容。', imagePath=getImagePath, toolbars="full",
                           filePath='bb/', blank=True, settings={"a": 2})







    
#定义用户特性    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    picture = models.ImageField(upload_to='profile_image', blank=True, null=True)

    def __unicode__(self):
		return self.user

    
        
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
    
	

		

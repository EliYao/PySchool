import datetime
from django.template.defaultfilters import slugify
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
		return self.user.username

class Folder(models.Model):
	title = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.title
        
        class Meta:
            ordering = ('title',)
                
        
class Course(models.Model):
    Folder = models.ManyToManyField(Folder)
    topic = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
	
    def __unicode__(self):
		return self.topic
        
    class Meta:
        ordering = ('topic',)
        
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
		
class CourseComments(models.Model):
    course = models.ForeignKey(Course)
    comment = models.CharField(max_length=140)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)	
    
    def __unicode__(self):
		return self.comment
    
	

		

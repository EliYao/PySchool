#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.contrib import admin
from school.models import UserProfile, Course, Folder, CourseComments,Lesson

class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('用户名',  {'fields':['user']}),
        ('头像',     {'fields':['picture']}),
    ]

class LessonAdmin(admin.ModelAdmin):
    list_display = ('course','title')

    
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('课程',{'fields':['Folder','topic','views','likes']}),
    ]
    
    inlines = [LessonInline]
    
    
class FolderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('课程夹名', {'fields':['title']}),
    ] 
    
    


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(CourseComments)
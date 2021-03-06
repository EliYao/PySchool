#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from school.forms import *
from school.models import *
from DjangoUeditor.forms import UEditorField 
from django.contrib.auth.models import User

@login_required
def searchResults(request):
    return render(request, 'school/searchResults.html')

@login_required    
def searchResults_c(request):
    return render(request, 'school/searchResults_c.html')
  
  
@login_required  
def index(request):
    
    return render(request, 'school/index.html')
    




@login_required   
def profileCenter(request):
    
    return render(request, 'school/profileCenter.html')



@login_required
def profileFolderDetails(request):
    
    return render(request, 'school/profileFolderDetails.html')

    
    
    
#创建课程    
@login_required
def createLesson(request):
    context = RequestContext(request)
    title = request.POST['title']
    return render(request, 'school/createLesson.html', {'title':title}, context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#课程内容定义    
@login_required    
def createLessonDefine(request):
    context = RequestContext(request)
    folderTitle = request.POST['folderTitle']
    if request.method == 'POST':
        title = request.POST['title']
        describe = request.POST['describe']
        
        if title and describe is not None:
              return render(request, 'school/createLessonDefine.html',{'title':title}, context)
        else:
           return render(request, 'school/createLesson.html', {'folderTitle':folderTitle}, context)
    else:
      return render(request, 'school/createLesson.html', {'folderTitle':folderTitle}, context)
 


 
#课程内容制作视频
@login_required    
def createLessonVideo(request):
    context = RequestContext(request)
    title = request.POST['title']
    if request.method == 'POST':
          title = request.POST['title']
          form = UEditorTestModelForm()
          return render(request, 'school/createLessonVideo.html',{'title':title,'form': form}, context)
    else:
      return render(request, 'school/createLessonDefine.html', {'title':title}, context)
    

@login_required    
def createLessonText(request):
    
    return render(request, 'school/createLessonText.html')

@login_required
def lessonDetails(request):
    
    return render(request, 'school/lessonDetails.html')

    
    
#用户注册
def signup(request):
    context = RequestContext(request)
    registered = False    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)       
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()        
        
    return render_to_response(
                    'school/signup.html',
                    {'user_form':user_form, 
                    'profile_form':profile_form, 
                    'registered': registered},context)
    
#退出
@login_required
def user_logout(request):
    logout(request)
    
    
    return HttpResponseRedirect('/school/')



#用户登录    
def user_login(request):
    model = UserProfile
    context = RequestContext(request)   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render_to_response('school/index.html', RequestContext(request,{}))

            else:
                return HttpResponse("帐号不存在！")
        
        else:
            print "Invaild login details: {0}, {1}".format(username, password)
            return HttpResponse("用户名或者密码不正确")

    else:
        return render(request, 'school/login.html', {}, context)

@login_required
def lessonStudy(request):
    return render(request, 'school/lessonStudy.html')
        
        
        
        
@login_required
def profileFolder(request):


    
    return render(request, 'school/profileFolder.html')

#课程添加
@login_required
def addCourse(request):
    context = RequestContext(request)
    title = request.POST['title']
    return render(request, 'school/addCourse.html', {'title':title}, context)

#课程夹添加    
@login_required    
def addFolder(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        title = request.POST['title']
        describe = request.POST['describe']
        
        if title and describe is not None:
              q = Folder(title=title, describe=describe)
              q.save()
              return render(request, 'school/addCourse.html',{'title':title}, context)
        else:
           return render(request, 'school/addFolder.html', {}, context)
    else:
      return render(request, 'school/addFolder.html', {}, context)
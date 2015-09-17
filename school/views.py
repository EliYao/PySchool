#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from school.forms import UserForm, UserProfileForm

@login_required
def ueditor(request):
    
	return render(request, 'school/multiEditorWithOneInstance.html')

@login_required  
def index(request):
    
    return render(request, 'school/index.html')
    
@login_required
def addCourse(request):
    
    return render(request, 'school/addCourse.html')

@login_required    
def addFolder(request):
    
    return render(request, 'school/addFolder.html')

@login_required   
def profileCenter(request):
    
    return render(request, 'school/profileCenter.html')

@login_required
def profileFolder(request):
    
    return render(request, 'school/profileFolder.html')

@login_required
def profileFolderDetails(request):
    
    return render(request, 'school/profileFolderDetails.html')

@login_required
def createLesson(request):
    
    return render(request, 'school/createLesson.html')

@login_required    
def createLessonDefine(request):
    
    return render(request, 'school/createLessonDefine.html')

@login_required    
def createLessonVideo(request):
    
    return render(request, 'school/createLessonVideo.html')

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
    context = RequestContext(request)   
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return render_to_response('school/index.html', context)

            else:
                return HttpResponse("帐号不存在！")
        
        else:
            print "Invaild login details: {0}, {1}".format(username, password)
            return HttpResponse("用户名或者密码不正确")

    else:
        return render(request, 'school/login.html', {}, context)
				

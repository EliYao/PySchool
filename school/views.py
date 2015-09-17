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


def ueditor(request):
    
	return render(request, 'school/multiEditorWithOneInstance.html')

def index(request):
    
	return render(request, 'school/index.html')
    
    
def login(request):
    
	return render(request, 'school/login.html')

def addCourse(request):
    
    return render(request, 'school/addCourse.html')
    
def addFolder(request):
    
    return render(request, 'school/addFolder.html')

   
def profileCenter(request):
    
    return render(request, 'school/profileCenter.html')

def profileFolder(request):
    
    return render(request, 'school/profileFolder.html')

def profileFolderDetails(request):
    
    return render(request, 'school/profileFolderDetails.html')

def createLesson(request):
    
    return render(request, 'school/createLesson.html')
    
def createLessonDefine(request):
    
    return render(request, 'school/createLessonDefine.html')
    
def createLessonVideo(request):
    
    return render(request, 'school/createLessonVideo.html')
    
def createLessonText(request):
    
    return render(request, 'school/createLessonText.html')

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
    



#用户登录    
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('school/index.html')
            else:
                return HttpResponse("帐号不存在！")
        
        else:
            print "Invaild login details: {0}, {1}".format(email, password)
            return HttpResponse("邮箱或者密码不正确")

    else:
        return render(request, 'school/index.html', {})
				

#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from school.forms import UserForm


def index(request):
    
	return render(request, 'school/index.html')
    
    
def login(request):
    
	return render(request, 'school/login.html')
    
    
def signup(request):
    
    return render(request, 'school/signup.html')    



    
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
				

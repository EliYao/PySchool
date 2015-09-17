#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from school.models import *
        
class UserForm(forms.ModelForm):
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')
    class  Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(label='头像',required=False)
    class Meta:
        model = UserProfile
        fields = ('picture',)

 
class TestUeditorModelForm(forms.ModelForm):
    class Meta:
      model = Blog
      fields = '__all__'
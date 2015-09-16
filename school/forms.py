#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from school.models import UserProfile, Blog
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email  = forms.CharField(widget=forms.TextInput())
    
    class  Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class TestUeditorModelForm(forms.ModelForm):
    class Meta:
      model = Blog
      fields = '__all__'
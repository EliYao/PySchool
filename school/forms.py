#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from school.models import *
  
class TestUEditorForm(forms.Form):
    Name = forms.CharField(label=u'姓名')
    ImagePath = forms.CharField()
    Description = UEditorField(u"描述", initial="abc", width=1000, height=300)
    Content = forms.CharField(label=u"内容",
                              widget=UEditorWidget({"width":600, "height":100, "imagePath":'aa', "filePath":'bb', "toolbars":"full"}))


  
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

      
class CreateFolderForm(forms.ModelForm):
    class Meta:
      model = Folder
      fields = ('title', 'describe')
"""
-- coding: utf-8 --
@Time : 2020/4/19 23:05
@Author : jcoool
@Site : 
@File : forms.py
@Software: PyCharm
"""
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)

class DynamicLoginForm(forms.Form):
    captcha = CaptchaField()

class DynamicRegisterForm(forms.Form):
    captcha = CaptchaField()
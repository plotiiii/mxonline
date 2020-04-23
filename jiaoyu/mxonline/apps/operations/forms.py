"""
-- coding: utf-8 --
@Time : 2020/4/24 0:28
@Author : jcoool
@Site : 
@File : forms.py
@Software: PyCharm
"""

import re

from django import forms
from apps.operations.models import UserFavorite, CourseComments


class UserFavForm(forms.ModelForm):
    class Meta:
        model = UserFavorite
        fields = ["fav_id", "fav_type"]


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CourseComments
        fields = ["course", "comments"]

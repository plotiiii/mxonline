"""
-- coding: utf-8 --
@Time : 2020/4/24 0:23
@Author : jcoool
@Site : 
@File : urls.py
@Software: PyCharm
"""
from django.conf.urls import url

from apps.operations.views import AddFavView

urlpatterns = [
    url(r'^fav/$', AddFavView.as_view(), name="fav"),
    # url(r'^comment/$', CommentView.as_view(), name="comment"),
]

"""
-- coding: utf-8 --
@Time : 2020/4/22 1:01
@Author : jcoool
@Site : 
@File : urls.py
@Software: PyCharm
"""
from django.conf.urls import url
from django.urls import path

from apps.organizations.views import OrgView,AddAskView,OrgHomeView,OrgTeacherView
urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name="list"),
    url(r'^add_ask/$', AddAskView.as_view(), name="add_ask"),
    url(r'^add_ask/$', AddAskView.as_view(), name="add_ask"),
    url(r'^(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="home"),
    url(r'^(?P<org_id>\d+)/teacher/$', OrgTeacherView.as_view(), name="teacher"),
    # url(r'^(?P<org_id>\d+)/course/$', OrgCourseView.as_view(), name="course"),
    # url(r'^(?P<org_id>\d+)/desc/$', OrgDescView.as_view(), name="desc"),

]
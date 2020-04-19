"""
-- coding: utf-8 --
@Time : 2020/4/19 13:27
@Author : jcoool
@Site : 
@File : xadmin.py
@Software: PyCharm
"""
import xadmin
from apps.courses.models import Course


class CoursesAadmin():
    pass


xadmin.site.register(Course, CoursesAadmin)

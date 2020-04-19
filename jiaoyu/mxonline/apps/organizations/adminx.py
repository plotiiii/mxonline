"""
-- coding: utf-8 --
@Time : 2020/4/19 13:27
@Author : jcoool
@Site : 
@File : xadmin.py
@Software: PyCharm
"""
import xadmin
from apps.organizations.models import Teacher,CourseOrg,City


class TeacherAadmin(object):
    pass

class CourseOrgAadmin(object):
    pass

class CityAadmin(object):
    pass



xadmin.site.register(Teacher, TeacherAadmin)
xadmin.site.register(CourseOrg, CourseOrgAadmin)
xadmin.site.register(City, CityAadmin)
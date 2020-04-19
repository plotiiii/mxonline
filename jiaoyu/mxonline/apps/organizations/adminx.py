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
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']


class CourseOrgAadmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums']
    style_fields = {
        "desc": "ueditor"
    }


class CityAadmin(object):
    list_display = ["id", "name", "desc"]
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "add_time"]
    list_editable = ["name", "desc"]



xadmin.site.register(Teacher, TeacherAadmin)
xadmin.site.register(CourseOrg, CourseOrgAadmin)
xadmin.site.register(City, CityAadmin)
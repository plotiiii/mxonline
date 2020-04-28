"""
-- coding: utf-8 --
@Time : 2020/4/19 13:27
@Author : jcoool
@Site : 
@File : xadmin.py
@Software: PyCharm
"""
import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource, CourseTag
from xadmin.layout import Fieldset, Main, Side, Row,FormActions
from import_export import resources


class GlobalSettings(object):
    site_title = "柳园G"
    site_footer = "柳园G413"
    # menu_style = "accordion"

class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'teacher']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    list_editable = ["degree", "desc"]

#固定的ip
#1. 本地的ip是一个动态分配的ip地址
#2. 数据包转发问题 scp
class NewCourseAdmin(object):
    # import_export_args = {'import_resource_class': MyResource, 'export_resource_class': MyResource}
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'teacher']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    list_editable = ["degree", "desc"]
    # readonly_fields = ["students", "add_time"]
    # exclude = ["click_nums", "fav_nums"]
    # ordering = ["click_nums"]
    # model_icon = 'fa fa-address-book'
    # inlines = [LessonInline, CourseResourceInline]
    # style_fields = {
    #     "detail":"ueditor"
    # }

    # def queryset(self):
    #     qs = super().queryset()
    #     if not self.request.user.is_superuser:
    #         qs = qs.filter(teacher=self.request.user.teacher)
    #     return qs

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                    Main(
                        Fieldset("讲师信息",
                                 'teacher','course_org',
                                 css_class='unsort no_title'
                                 ),
                        Fieldset("基本信息",
                                 'name', 'desc',
                                 Row('learn_times', 'degree'),
                                 Row('category', 'tag'),
                                 'youneed_know', 'teacher_tell', 'detail',
                                 ),
                    ),
                    Side(
                        Fieldset("访问信息",
                                 'fav_nums', 'click_nums', 'students','add_time'
                                 ),
                    ),
                    Side(
                        Fieldset("选择信息",
                                 'is_banner', 'is_classics'
                                 ),
                    )
            )
        return super(NewCourseAdmin, self).get_form_layout()


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'add_time']

class CourseTagAdmin(object):
    list_display = ['course', 'tag','add_time']
    search_fields = ['course', 'tag']
    list_filter = ['course', 'tag','add_time']

# xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Course, NewCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(CourseTag, CourseTagAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)

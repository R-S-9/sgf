from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

from .models import (
    TrainingCourse, Review, CourseComposition, CourseProgram
)


class MyAdminSite(AdminSite):
    """Сортируем модели в admin для удобства"""
    def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_list = sorted(
            self._build_app_dict(request).values(),
            key=lambda x: x['name'].lower()
        )

        return app_list


admin.site = MyAdminSite()

admin.site.register(TrainingCourse)
admin.site.register(CourseComposition)
admin.site.register(CourseProgram)
admin.site.register(Review)

admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)

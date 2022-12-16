from rest_framework.routers import DefaultRouter

from apps.account.viewsets import TeacherViewSet
from apps.feed.viewsets import CoursesViewSet


router = DefaultRouter()

router.register(r"teacher", TeacherViewSet, basename="teacher")
router.register(r"courses", CoursesViewSet, basename="courses")

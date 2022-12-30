from rest_framework.routers import DefaultRouter

from apps.account.viewsets import TeacherViewSet
from apps.feed.viewsets import CoursesViewSet, ReviewsViewSet


router = DefaultRouter()

router.register(r"teachers", TeacherViewSet, basename="teachers")
router.register(r"courses", CoursesViewSet, basename="courses")
router.register(r"reviews", ReviewsViewSet, basename="Reviews")

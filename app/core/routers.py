from rest_framework.routers import DefaultRouter

from apps.account.viewsets import TeacherViewSet, UserViewSet
from apps.feed.viewsets import (
    CoursesViewSet,
    ReviewsViewSet,
    CourseProgramViewSet,
    CourseCompositionViewSet,
)


router = DefaultRouter()

# account
router.register(r"teachers", TeacherViewSet, basename="teachers")
router.register(r'users', UserViewSet, basename='users')

# feed
router.register(r"courses", CoursesViewSet, basename="courses")
router.register(r"reviews", ReviewsViewSet, basename="Reviews")
router.register(
    "course_program", CourseProgramViewSet, basename="course_program"
)
router.register(
    r"course_composition",
    CourseCompositionViewSet,
    basename="course_composition"
)

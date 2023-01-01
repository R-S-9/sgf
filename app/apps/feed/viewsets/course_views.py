from rest_framework import viewsets, mixins
from apps.account.user_permissions.permissions import IsUserOrReadOnly

from ..models import (
    TrainingCourse,
    CourseComposition,
    CourseProgram
)
from ..serializers import (
    TrainingCourseSerializer,
    CourseProgramSerializer,
    CourseCompositionSerializer,
)


class CoursesViewSet(
    viewsets.ModelViewSet
):
    """Список курсов"""
    queryset = TrainingCourse.objects.all()
    serializer_class = TrainingCourseSerializer
    permission_classes = (IsUserOrReadOnly,)


class CourseProgramViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Список 'в курс входят'"""
    queryset = CourseProgram.objects.all()
    serializer_class = CourseProgramSerializer
    permission_classes = (IsUserOrReadOnly,)


class CourseCompositionViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Список 'программы курса'"""
    queryset = CourseComposition.objects.all()
    serializer_class = CourseCompositionSerializer
    permission_classes = (IsUserOrReadOnly,)

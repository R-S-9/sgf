from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import TrainingCourse
from ..serializers import TrainingCourseSerializer


class CoursesViewSet(viewsets.ReadOnlyModelViewSet):
    """Список курсов"""
    queryset = TrainingCourse.objects.all()
    serializer_class = TrainingCourseSerializer
    permission_classes = (AllowAny,)

from rest_framework import viewsets

from ..models import TrainingCourse
from ..serializers import TrainingCourseSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = TrainingCourse.objects.all()
    serializer_class = TrainingCourseSerializer

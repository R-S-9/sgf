from rest_framework import viewsets

from ..models import Teacher
from ..serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    # prefetch_related("reading_group" or "reading__group__...")
    serializer_class = TeacherSerializer

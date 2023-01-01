from django.http import JsonResponse
from rest_framework import viewsets

from ..models import Teacher
from ..serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    # prefetch_related("reading_group" or "reading__group__...")
    serializer_class = TeacherSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(
            data={"data": "user create successfully"}, status=201
        )

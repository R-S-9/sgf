from rest_framework.routers import DefaultRouter

from ..serializers.teacher_serializer import TeacherSerializer


app_name = "api"
router = DefaultRouter()

router.register("create_user", TeacherSerializer, "create_user")

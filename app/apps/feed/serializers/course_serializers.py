from rest_framework import serializers

from ..models import TrainingCourse


class TrainingCourseSerializer(serializers.ModelSerializer):
    # rating_avg = serializers.IntegerField()

    class Meta:
        model = TrainingCourse
        fields = "__all__"
        # fields = ('user','name','description','for_whom',)

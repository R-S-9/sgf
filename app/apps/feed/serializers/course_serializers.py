from rest_framework import serializers
from django.db.models import Avg

from ..models import TrainingCourse, CourseComposition, CourseProgram


class CourseCompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComposition
        fields = '__all__'


class CourseProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgram
        fields = '__all__'

class TrainingCourseSerializer(serializers.ModelSerializer):
    course_program = CourseProgramSerializer(
        many=True, source='courseprogram_set', read_only=True
    )
    course_composition = CourseCompositionSerializer(
        many=True, source='coursecomposition_set', read_only=True
    )
    average_rating = serializers.SerializerMethodField(read_only=True)

    def get_average_rating(self, obj):
        return obj.reviews.all().aggregate(Avg('rating'))['rating__avg']

    class Meta:
        model = TrainingCourse
        fields = (
            'user',
            'name',
            'description',
            'requirement',
            'price',
            'level_training',
            'all_participant',
            'main_image',
            'date_create',
            'modified',
            'course_program',
            'course_composition',
            'average_rating',
        )

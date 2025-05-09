from rest_framework import serializers


# code here
from rest_framework import serializers
from .models import School, Classroom, Teacher, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'short_name', 'address']


class SchoolDetailSerializer(SchoolSerializer):

    class Meta(SchoolSerializer.Meta):
        fields = SchoolSerializer.Meta.fields + [
            'classroom_count',
            'teacher_count',
            'student_count',
        ]


class ClassroomSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), write_only=True
    )
    school_detail = SchoolSerializer(source='school', read_only=True)

    class Meta:
        model = Classroom
        fields = [
            'id',
            'grade',
            'room',
            'school',
            'school_detail',
        ]


class TeacherSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), write_only=True
    )
    classroom_detail = ClassroomSerializer(
        source='classroom', read_only=True, many=True
    )
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), write_only=True
    )
    school_detail = SchoolSerializer(source='school', read_only=True)

    class Meta:
        model = Teacher
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'classroom',
            'classroom_detail',
            'school',
            'school_detail',
        ]

    def create(self, validated_data):
        classroom_ids = validated_data.pop('classroom')
        teacher = Teacher.objects.create(**validated_data)
        for classroom_id in classroom_ids:
            classroom = Classroom.objects.get(pk=classroom_id)
            if not classroom:
                raise serializers.ValidationError({'detail': 'Classroom not found'})
            teacher.classroom.add(classroom)
        return teacher

    def update(self, instance, validated_data):
        classroom_ids = validated_data.pop('classroom')
        instance.classroom.clear()
        for classroom_id in classroom_ids:
            classroom = Classroom.objects.get(pk=classroom_id)
            if not classroom:
                raise serializers.ValidationError({'detail': 'Classroom not found'})
            instance.classroom.add(classroom)
        return super().update(instance, validated_data)


class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), write_only=True
    )
    classroom_detail = ClassroomSerializer(source='classroom', read_only=True)
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), write_only=True
    )
    school_detail = SchoolSerializer(source='school', read_only=True)

    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'classroom',
            'classroom_detail',
            'school',
            'school_detail',
        ]

from rest_framework import serializers
from .models import School, Classroom, Teacher, Student

# code here


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
    class Meta:
        model = Classroom
        fields = [
            'id',
            'grade',
            'room',
            'school',
        ]
        depth = 1


class ClassroomCreateSerializer(ClassroomSerializer):
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), write_only=True
    )


class ClassroomDetailSerializer(ClassroomSerializer):
    school = serializers.ReadOnlyField(source='school.name')

    class Meta(ClassroomSerializer.Meta):
        fields = [
            'id',
            'grade',
            'room',
            'school',
            'list_of_teacher',
            'list_of_student',
        ]


class TeacherSerializer(serializers.ModelSerializer):
    school = serializers.ReadOnlyField(source='school.name')
    classrooms = serializers.SerializerMethodField()

    @staticmethod
    def get_classrooms(obj):
        return [classroom.room for classroom in obj.classrooms.all()]

    class Meta:
        model = Teacher
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'school',
            'classrooms',
        ]


class TeacherDetailSerializer(TeacherSerializer):
    class Meta(TeacherSerializer.Meta):
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'school',
            'list_of_classroom',
        ]


class TeacherCreateSerializer(TeacherSerializer):
    classrooms = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), write_only=True, many=True, allow_empty=True
    )
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), write_only=True
    )

    def create(self, validated_data):
        classroom_ids = validated_data.pop('classrooms')
        teacher = Teacher.objects.create(**validated_data)
        if not classroom_ids:
            raise serializers.ValidationError({'detail': 'Classroom not found'})
        for classroom in classroom_ids:
            teacher.classrooms.add(classroom)
        return teacher

    def update(self, instance, validated_data):
        classroom_ids = validated_data.pop('classrooms')
        if not classroom_ids:
            raise serializers.ValidationError({'detail': 'Classroom not found'})
        instance.classrooms.clear()
        for classroom in classroom_ids:
            instance.classrooms.add(classroom)
        return super().update(instance, validated_data)


class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.ReadOnlyField(source='classroom.room')
    school = serializers.ReadOnlyField(source='school.name')

    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'classroom',
            'school',
        ]


class StudentDetailSerializer(StudentSerializer):
    class Meta(StudentSerializer.Meta):
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'school',
            'classroom_detail',
        ]


class StudentCreateSerializer(StudentSerializer):
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), write_only=True
    )
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(), write_only=True
    )

    def create(self, validated_data):
        classroom = validated_data.pop('classroom')
        if not classroom:
            raise serializers.ValidationError({'detail': 'Classroom not found'})
        student = Student.objects.create(classroom=classroom, **validated_data)
        return student

    def update(self, instance, validated_data):
        classroom = validated_data.pop('classroom')
        if not classroom:
            raise serializers.ValidationError({'detail': 'Classroom not found'})
        instance.classroom_id = classroom.id
        return super().update(instance, validated_data)

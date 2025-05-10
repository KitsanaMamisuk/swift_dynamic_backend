from django.db import models
from .choices import Gender, Grade, Room


class School(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    short_name = models.CharField(max_length=255, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'short_name'], name='unique_name_short_name_school'
            )
        ]

    @property
    def classroom_count(self):
        return self.classrooms.count()

    @property
    def teacher_count(self):
        return self.teachers.count()

    @property
    def student_count(self):
        return self.students.count()


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(choices=Gender.choices, default=Gender.MALE)
    school = models.ForeignKey(
        School, on_delete=models.SET_NULL, related_name='teachers',
        null=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name'],
                name='unique_first_name_last_name_teacher',
            )
        ]

    @property
    def list_of_classroom(self):
        return [
            {'id': classroom.id, 'grade': classroom.grade, 'room': classroom.room}
            for classroom in self.classrooms.all()
        ]


class Classroom(models.Model):
    grade = models.CharField(choices=Grade.choices, default=Grade.GRADE_ONE)
    room = models.CharField(choices=Room.choices, default=Room.GRADE_ONE_ROOM_ONE)
    school = models.ForeignKey(
        School, on_delete=models.SET_NULL, related_name='classrooms',
        null=True
    )
    teacher = models.ManyToManyField(Teacher, related_name='classrooms')

    def __str__(self):
        return f'Grade: {self.room}'

    @property
    def list_of_teacher(self):
        return [
            {
                'id': teacher.id,
                'first_name': teacher.first_name,
                'last_name': teacher.last_name,
                'gender': teacher.gender,
            }
            for teacher in self.teacher.all()
        ]

    @property
    def list_of_student(self):
        return [
            {
                'id': student.id,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'gender': student.gender,
            }
            for student in self.students.all()
        ]


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(choices=Gender.choices, default=Gender.MALE)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.SET_NULL, related_name='students',
        null=True
    )
    school = models.ForeignKey(
        School, on_delete=models.SET_NULL, related_name='students',
        null=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name'],
                name='unique_first_name_last_name_student',
            )
        ]

    @property
    def classroom_detail(self):
        return {
            'id': self.classroom.id,
            'grade': self.classroom.grade,
            'room': self.classroom.room,
            'teachers': [
                {
                    'id': teacher.id,
                    'first_name': teacher.first_name,
                    'last_name': teacher.last_name,
                    'gender': teacher.gender,
                }
                for teacher in self.classroom.teacher.all()
            ],
        }

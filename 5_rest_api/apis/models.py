from django.db import models
from .choices import Gender, Grade
# Create your models here.
#### โรงเรียน(school)

# - ชื่อโรงเรียน
# - ตัวย่อชื่อโรงเรียน
# - ที่อยู่

# #### ห้องเรียน(classroom)

# - ชั้นปี
# - ทับ

# #### ครู(teacher)

# - ชื่อ
# - นามสกุล
# - เพศ

# #### นักเรียน(student)

# - ชื่อ
# - นามสกุล
# - เพศ

#โดยครูจะสามารถอยู่ได้หลายห้องเรียน และแต่ละห้องเรียนก็สามารมีครูได้หลายคน  ในส่วนของนักเรียนสามารถอยู่ได้เพียงห้องเรียนเดียวและในแต่ละห้องเรียนสามารถมีนักเรียนได้หลายคน**

class School(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    short_name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'short_name'], name='unique_name_short_name_school')
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
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_first_name_last_name_teacher')
        ]
        

class Classroom(models.Model):
    grade = models.CharField(choices=Grade.choices, default=Grade.GRADE_ONE)
    room = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    teacher = models.ManyToManyField(Teacher)
    
    def __str__(self):
        return f'Grade: {self.grade}/{self.room}'
    
    
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(choices=Gender.choices, default=Gender.MALE)
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE, related_name='students')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_first_name_last_name_student')
        ]
        
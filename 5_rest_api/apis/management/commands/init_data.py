import random
from django.core.management.base import BaseCommand
from faker import Faker
from apis.models import School, Classroom, Teacher, Student
from apis.choices import Grade, Room

fake = Faker('th_TH')


class Command(BaseCommand):
    help = 'Create mock data to db'

    def handle(self, *args, **kwargs):
        try:
            # create school
            print('Create mock data school')
            schools = []
            for _ in range(10):
                name = f'โรงเรียน{fake.name()}วิทยา'.replace(' ', '')
                short_name = short_name = fake.unique.pystr_format(
                    string_format='???'
                ).upper()
                address = fake.address()
                schools.append(
                    School(name=name, short_name=short_name, address=address)
                )
            School.objects.bulk_create(schools)
            print('.')
            print('Create mock data school success')
        except Exception as e:
            print(f'Can not create mock data school : {e}')

        try:
            # create classroom
            print('.')
            print('.')
            print('Create mock data classroom')
            classrooms = []
            for school in School.objects.all():
                for grade in [
                    Grade.GRADE_ONE,
                    Grade.GRADE_TWO,
                    Grade.GRADE_THREE,
                    Grade.GRADE_FOUR,
                    Grade.GRADE_FIVE,
                    Grade.GRADE_SIX,
                ]:
                    for room in range(1, 4):
                        classrooms.append(
                            Classroom(
                                grade=grade,
                                room=dict(Room.choices)[f'{grade}/{room}'],
                                school=school,
                            )
                        )
            Classroom.objects.bulk_create(classrooms)
            print('.')
            print('Create mock data classroom success')
        except Exception as e:
            print(f'Can not create mock data classroom : {e}')

        try:
            # create teacher
            print('.')
            print('.')
            print('Create mock data teacher')
            prefix_name_female = ['นาง', 'นางสาว']
            teachers = []
            schools = School.objects.prefetch_related('classrooms').all()
            for school in schools:
                classrooms = school.classrooms.all()
                for classroom in classrooms:
                    for _ in range(2):
                        gender = fake.random_element(elements=('M', 'F'))
                        if gender == 'M':
                            first_name = f'นาย{fake.first_name_male()}{fake.word()}'
                            last_name = f'{fake.last_name_male()}{fake.city()}'
                        else:
                            index = random.randint(0, 1)
                            first_name = f'{prefix_name_female[index]}{fake.word()}'
                            last_name = f'{fake.last_name_female()}{fake.city()}'

                        teachers.append(
                            Teacher(
                                first_name=first_name,
                                last_name=last_name,
                                gender=gender,
                                school=school,
                            )
                        )
            instance_bulk = Teacher.objects.bulk_create(teachers)
            for school in schools:
                school_teachers = [
                    teacher
                    for teacher in instance_bulk
                    if teacher.school_id == school.id
                ]
                classrooms = school.classrooms.all()
                for classroom in classrooms:
                    selected_teachers = random.sample(school_teachers, 3)
                    classroom.teacher.add(*selected_teachers)
            print('.')
            print('Create mock data teacher success')
        except Exception as e:
            print(f'Can not create mock data teacher : {e}')

        try:
            # create student
            print('.')
            print('.')
            print('Create mock data student')
            students = []
            prefix_name_male = ['เด็กชาย', 'นาย']
            prefix_name_female = ['เด็กหญิง', 'นางสาว']
            schools = School.objects.prefetch_related('classrooms').all()
            for school in schools:
                classrooms = school.classrooms.all()
                for classroom in classrooms:
                    for _ in range(10):
                        gender = fake.random_element(elements=('M', 'F'))
                        if gender == 'M':
                            index = random.randint(0, 1)
                            first_name = f'{prefix_name_male[index]}{fake.first_name_male()}{fake.word()}'
                            last_name = f'{fake.last_name_male()}{fake.city()}'
                        else:
                            index = random.randint(0, 1)
                            first_name = f'{prefix_name_female[index]}{fake.first_name_female()}{fake.word()}'
                            last_name = f'{fake.last_name_female()}{fake.city()}'
                        students.append(
                            Student(
                                first_name=first_name,
                                last_name=last_name,
                                gender=gender,
                                classroom=classroom,
                                school=school,
                            )
                        )
            Student.objects.bulk_create(students)
            print('.')
            print('Create mock data student success')
        except Exception as e:
            print(f'Can not create mock data student : {e}')

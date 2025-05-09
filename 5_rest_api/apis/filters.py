from django_filters import FilterSet, filters
from .models import School, Classroom, Teacher, Student
from django.db.models import Q

# code here


class SchoolFilter(FilterSet):
    name = filters.CharFilter(method='filter_name', label='Name of school')

    @staticmethod
    def filter_name(queryset, name, value):
        # Handle the filtering by list of names
        name_list = value.split(',')
        q = Q()
        for name in name_list:
            q |= Q(name__icontains=name)
        return queryset.filter(q)

    class Meta:
        model = School
        fields = ['name']


class ClassroomFilter(FilterSet):
    school = filters.CharFilter(method='filter_school', label='Room of school')

    @staticmethod
    def filter_school(queryset, name, value):
        school_list = value.split(',')
        q = Q()
        for school in school_list:
            q |= Q(school__name__icontains=school)
        return queryset.filter(q)

    class Meta:
        model = Classroom
        fields = ['school']


class TeacherFilter(FilterSet):
    school = filters.CharFilter(method='filter_school', label='Name of school')
    classroom = filters.CharFilter(method='filter_classroom', label='Classroom')
    first_name = filters.CharFilter(method='filter_first_name', label='First Name')
    last_name = filters.CharFilter(method='filter_last_name', label='Last Name')
    gender = filters.CharFilter(method='filter_gender', label='Gender')

    @staticmethod
    def filter_first_name(queryset, name, value):
        first_name_list = value.split(',')
        q = Q()
        for first_name in first_name_list:
            q |= Q(first_name__icontains=first_name)
        return queryset.filter(q)

    @staticmethod
    def filter_last_name(queryset, name, value):
        last_name_list = value.split(',')
        q = Q()
        for last_name in last_name_list:
            q |= Q(last_name__icontains=last_name)
        return queryset.filter(q)

    @staticmethod
    def filter_gender(queryset, name, value):
        gender_list = value.split(',')
        q = Q()
        for gender in gender_list:
            q |= Q(gender__icontains=gender)
        return queryset.filter(q)

    @staticmethod
    def filter_school(queryset, name, value):
        school_list = value.split(',')
        q = Q()
        for school in school_list:
            q |= Q(school__name__icontains=school)
        return queryset.filter(q)

    @staticmethod
    def filter_classroom(queryset, name, value):
        # Handle the filtering by list of names
        classroom_list = value.split(',')
        q = Q()
        for classroom in classroom_list:
            q |= Q(classrooms__room__icontains=classroom)
        return queryset.filter(q)

    class Meta:
        model = Teacher
        fields = ['classroom', 'school', 'first_name', 'last_name', 'gender']


class StudentFilter(FilterSet):
    school = filters.CharFilter(method='filter_school', label='Name of school')
    classroom = filters.CharFilter(method='filter_classroom', label='Classroom')
    first_name = filters.CharFilter(method='filter_first_name', label='First Name')
    last_name = filters.CharFilter(method='filter_last_name', label='Last Name')
    gender = filters.CharFilter(method='filter_gender', label='Gender')

    @staticmethod
    def filter_first_name(queryset, name, value):
        first_name_list = value.split(',')
        q = Q()
        for first_name in first_name_list:
            q |= Q(first_name__icontains=first_name)
        return queryset.filter(q)

    @staticmethod
    def filter_last_name(queryset, name, value):
        last_name_list = value.split(',')
        q = Q()
        for last_name in last_name_list:
            q |= Q(last_name__icontains=last_name)
        return queryset.filter(q)

    @staticmethod
    def filter_gender(queryset, name, value):
        gender_list = value.split(',')
        q = Q()
        for gender in gender_list:
            q |= Q(gender__icontains=gender)
        return queryset.filter(q)

    @staticmethod
    def filter_school(queryset, name, value):
        school_list = value.split(',')
        q = Q()
        for school in school_list:
            q |= Q(school__name__icontains=school)
        return queryset.filter(q)

    @staticmethod
    def filter_classroom(queryset, name, value):
        # Handle the filtering by list of names
        classroom_list = value.split(',')
        q = Q()
        for classroom in classroom_list:
            q |= Q(classroom__room__icontains=classroom)
        return queryset.filter(q)

    class Meta:
        model = Student
        fields = ['classroom', 'school', 'first_name', 'last_name', 'gender']

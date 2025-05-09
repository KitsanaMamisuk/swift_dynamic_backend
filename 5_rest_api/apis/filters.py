from django_filters import FilterSet, filters
from .models import School, Classroom, Teacher, Student
from django.db.models import Q

# code here

class SchoolFilter(FilterSet):
    name = filters.CharFilter(method='filter_name')
    
    def filter_name(self, queryset, name, value):
        # Handle the filtering by list of names
        name_list = value.split(',')
        q = Q()
        for name in name_list:
            q |= Q(name__icontains=name)
        return queryset.filter(q)
    
    class Meta:
        model = School
        fields = ['name']
        
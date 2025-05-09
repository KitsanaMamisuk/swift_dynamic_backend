from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apis.models import School
from apis.serializers import SchoolSerializer, SchoolDetailSerializer
from rest_framework.permissions import AllowAny
from apis.filters import SchoolFilter
# from rest_framework import status



# todo
# [x] school list
#   can filter with
#   [x] name
# [x] school detail
#   in detail want to know
#   [x] count of classroom
#   [x] count of teacher
#   [x] count of student
# - update school
# - delete school


class SchoolViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = None
    queryset = None
    filterset_class = SchoolFilter
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SchoolDetailSerializer
        return SchoolSerializer
    
    def get_queryset(self):
        queryset = School.objects.prefetch_related('classrooms', 'teachers', 'students').all().order_by('id')
        return queryset
    
    
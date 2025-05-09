from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apis.models import Student
from apis.serializers import (
    StudentSerializer,
    StudentDetailSerializer,
    StudentCreateSerializer,
)
from rest_framework.permissions import AllowAny
from apis.filters import StudentFilter
from rest_framework import status


class StudentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = None
    queryset = None
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return StudentCreateSerializer
        return StudentSerializer

    def get_queryset(self):
        queryset = (
            Student.objects.prefetch_related('school', 'classroom').all().order_by('id')
        )
        return queryset

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(
            {'detail': 'Created successfully'}, status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({'detail': 'Updated successfully'}, status=status.HTTP_200_OK)

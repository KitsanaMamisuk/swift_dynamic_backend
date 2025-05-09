from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apis.models import Teacher
from apis.serializers import (
    TeacherCreateSerializer,
    TeacherSerializer,
    TeacherDetailSerializer,
)
from rest_framework.permissions import AllowAny
from apis.filters import TeacherFilter
from rest_framework import status


class TeacherViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = None
    queryset = None
    filterset_class = TeacherFilter

    def get_queryset(self):
        queryset = (
            Teacher.objects.prefetch_related('classrooms', 'school')
            .all()
            .order_by('id')
        )
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return TeacherCreateSerializer
        return TeacherSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(
            {'detail': 'Created successfully'}, status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response({'detail': 'Updated successfully'}, status=status.HTTP_200_OK)

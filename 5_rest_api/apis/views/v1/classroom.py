from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apis.models import Classroom
from apis.serializers import (
    ClassroomDetailSerializer,
    ClassroomSerializer,
    ClassroomCreateSerializer,
)
from rest_framework.permissions import AllowAny
from apis.filters import ClassroomFilter
from rest_framework import status


class ClassroomViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = None
    queryset = None
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ClassroomCreateSerializer
        return ClassroomSerializer

    def get_queryset(self):
        queryset = (
            Classroom.objects.prefetch_related('teacher', 'students', 'school')
            .all()
            .order_by('id')
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

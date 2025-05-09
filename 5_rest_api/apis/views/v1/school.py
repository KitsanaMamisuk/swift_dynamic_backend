from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apis.models import School
from apis.serializers import SchoolSerializer, SchoolDetailSerializer
from rest_framework.permissions import AllowAny
from apis.filters import SchoolFilter
from rest_framework import status


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
        queryset = (
            School.objects.prefetch_related('classrooms', 'teachers', 'students')
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

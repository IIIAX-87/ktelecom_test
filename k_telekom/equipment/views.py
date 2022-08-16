import django_filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .models import Equipment, EquipmentType
from .serializers import EquipmentSerializer, EquipmentTypeSerializer
from .service import create_equipments, update_equipment


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'

    permission_classes = [permissions.IsAuthenticated]

    def create(self, request,  *args, **kwargs):
        print(request.data)
        return Response(create_equipments(request.data))

    def update(self, request, *args, **kwargs):
        print(request.data)
        return Response(update_equipment(request))


class EquipmentTypeViewSet(viewsets.ModelViewSet):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

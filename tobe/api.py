from.models import Tobe
from.filters import TobeFilter
from.serializers import TobeSerializers
from rest_framework import filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class TobeViewset(viewsets.ModelViewSet):
    queryset = Tobe.objects.all()
    serializer_class = TobeSerializers
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_class = TobeFilter     
    ordering_fields = ['id']  
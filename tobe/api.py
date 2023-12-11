from.models import Tobe
from.serializers import TobeSerializers
from rest_framework import viewsets

from.filters import TobeFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class TobeViewset(viewsets.ModelViewSet):
    queryset = Tobe.objects.all()
    serializer_class = TobeSerializers
    filter_backends = [DjangoFilterBackend]         # django filter search
    filterset_fields = ['name','description','status']            # django filter search
 
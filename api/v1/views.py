from rest_framework import viewsets

from common.models import File
from . import serializers


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = serializers.FileSerializer

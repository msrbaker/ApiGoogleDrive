from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from common.models import File
from api.v1 import serializers


class FileViewSet(viewsets.ModelViewSet):
    """API endpoint that lists files and accepts new files."""
    queryset = File.objects.all()
    serializer_class = serializers.FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        file_ = request.data.get('file')
        if file_:
            # There's a strange issue with the GDrive API and file names with
            # dashes, so replace them
            file_.name = file_.name.replace('-', '_')
            request.data['file'] = file_
        file_serializer = self.serializer_class(data=request.data)
        if file_serializer.is_valid():
                return super().create(request, *args, **kwargs)
        # The specs incorrectly require 404, so I leave this here just in case
        # return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(file_serializer.errors, status=status.HTTP_404_NOT_FOUND)


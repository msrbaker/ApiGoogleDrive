from rest_framework import serializers

from common.models import File


class FileSerializer(serializers.HyperlinkedModelSerializer):
    """Model serializer for files."""
    class Meta:
        model = File
        fields = ('titulo', 'descripcion', 'file')

from oauth2client import file, client, tools
from googleapiclient.discovery import build
from httplib2 import Http

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import views, viewsets
from rest_framework import status
from django.conf import settings

from common.models import File
from api.v1 import serializers


class SearchInDocView(views.APIView):
    SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'

    def get(self, request, file_id=None):
        word = request.GET.get('word')
        if file_id and word:
            store = file.Storage('token.json')
            creds = store.get()
            if not creds or creds.invalid:
                flow = client.flow_from_clientsecrets(
                    settings.GDRIVE_CREDS_OAUTH_FILE,
                    self.SCOPES
                )
                creds = tools.run_flow(flow, store)
            service = build('drive', 'v3', http=creds.authorize(Http()))

            # Call the Drive v3 API
            # https://developers.google.com/drive/api/v3/reference/files/list
            # https://developers.google.com/drive/api/v3/search-parameters
            results = service.files().list(
                fields="nextPageToken, files(id, name)",
                q="fullText contains '{}'".format(word)
            ).execute()
            items = results.get('files', [])
            for item in items:
                if item['id'] == file_id:
                    return Response(item, status.HTTP_200_OK)

            return Response('File not found', status.HTTP_404_NOT_FOUND)
        return Response('Usage: /<id>?word=<search term>',
                        status=status.HTTP_400_BAD_REQUEST)


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


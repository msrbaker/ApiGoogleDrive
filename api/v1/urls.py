from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'v1'

router = routers.DefaultRouter()

router.register('file', views.FileViewSet)

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]

from django.shortcuts import render
from rest_framework import viewsets
from .models import VideoElement
from .serializers import Video_Element_Serializer

# Create your views here.

class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoElement.objects.all()
    serializer_class = Video_Element_Serializer
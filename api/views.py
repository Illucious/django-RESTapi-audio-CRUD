from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import VideoElement, Audio_Element
from .serializers import Video_Element_Serializer, Audio_Element_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def index(request):
    return render(request, "index.html")


@api_view(["GET", "POST"])
def video_element(request):
    if request.method == "GET":
        video_element = VideoElement.objects.all()
        serializer = Video_Element_Serializer(video_element, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = Video_Element_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "DELETE"])
def audio_element_get_delete_by_videoID(request, fk):
    if request.method == "GET":
        audio_element = Audio_Element.objects.filter(video_element_id=fk)
        serializer = Audio_Element_Serializer(audio_element, many=True)
        return Response(serializer.data)

    elif request.method == "DELETE":
        audio_element = Audio_Element.objects.filter(video_element_id=fk)
        audio_element.delete()
        return Response("Deleted")


@api_view(["POST"])
def audio_element_post(request):
    if request.method == "POST":
        serializer = Audio_Element_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["PUT", "DELETE", "GET"])
def audio_element_put_delete_get_by_audio_id(request, pk):
    if request.method == "PUT":
        audio_element = Audio_Element.objects.get(audio_element_id=pk)
        serializer = Audio_Element_Serializer(audio_element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        audio_element = Audio_Element.objects.get(audio_element_id=pk)
        audio_element.delete()
        return Response("Deleted")
    elif request.method == "GET":
        audio_element = Audio_Element.objects.get(audio_element_id=pk)
        serializer = Audio_Element_Serializer(audio_element, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def audio_fragment_view(request):
    start_time = request.query_params.get('start_time')
    end_time = request.query_params.get('end_time')

    audio_elements = Audio_Element.objects.filter(
        start_time__gte=start_time, end_time__lte=end_time)
    serializer = Audio_Element_Serializer(audio_elements, many=True)

    return Response(serializer.data)

from rest_framework import serializers
from .models import VideoElement, Audio_Element


class Video_Element_Serializer(serializers.ModelSerializer):
    video_element_id = serializers.ReadOnlyField()
    class Meta:
        model = VideoElement
        fields = '__all__'


class Audio_Element_Serializer(serializers.ModelSerializer):
    audio_element_id = serializers.ReadOnlyField()
    class Meta:
        model = Audio_Element
        fields = ('audio_element_id', 'url', 'high_volume', 'low_volume', 'audio_element_type', 'video_element_id', 'duration')
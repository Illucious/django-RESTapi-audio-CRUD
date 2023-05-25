from rest_framework import serializers
from .models import VideoElement


class Video_Element_Serializer(serializers.ModelSerializer):
    video_element_id = serializers.ReadOnlyField()
    class Meta:
        model = VideoElement
        fields = '__all__'
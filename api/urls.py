from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import index, video_element, audio_element_get_delete_by_videoID, audio_element_post, audio_element_put_delete_get_by_audio_id, audio_fragment_view


urlpatterns = [
    path("", index, name="index"),
    path("video-element/", video_element, name="video_element"),
    path("video-element-audio-elements/<int:fk>/",
         audio_element_get_delete_by_videoID, name="audio_element_get_delete"),
    path("audio-element/", audio_element_post, name="audio_element_post"),
    path("audio-element/<int:pk>/", audio_element_put_delete_get_by_audio_id,
         name="audio_element_put_delete_get_by_audio_id"),
    path("audio-fragments/", audio_fragment_view, name="audio_element_post"),
]

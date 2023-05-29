from django.db import models

# Create your models here.


class VideoElement(models.Model):
    video_element_id = models.AutoField(primary_key=True)
    video_url = models.URLField(max_length=200, null=True, blank=True)


class Audio_Element(models.Model):
    choices = (
        ("vo", "voice-over"),
        ("bg_music", "background-music"),
        ("video_music", "video-music"),
    )

    audio_element_id = models.AutoField(primary_key=True)
    audio_element_type = models.CharField(choices=choices, max_length=20)
    high_volume = models.IntegerField()
    low_volume = models.IntegerField()
    video_element_id = models.ForeignKey(
        VideoElement, on_delete=models.CASCADE, null=True, blank=True
    )
    url = models.URLField(max_length=200, null=True, blank=True)
    start_time = models.FloatField(null=True, blank=True)
    end_time = models.FloatField(null=True, blank=True)

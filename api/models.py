from django.db import models

# Create your models here.


class VideoElement(models.Model):
    video_element_id = models.AutoField(primary_key=True)
    video_element_duration = models.IntegerField()
    video_element_upload_time = models.DateTimeField(auto_now_add=True)


"""class Audio_Element(models.Model):
    audio_element_id = models.AutoField(primary_key=True)
    audio_element_type = models.CharField(max_length=10,)
    high_volume = models.IntegerField()
    low_volume = models.IntegerField()
    video_element_id = models.ForeignKey(Video_Element, on_delete=models.CASCADE, null=True, blank=True)"""
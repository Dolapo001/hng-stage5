from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')


class VideoTranscription(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    transcription = models.TextField()

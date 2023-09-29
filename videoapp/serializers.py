from rest_framework import serializers
from .models import Video, VideoTranscription


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'video_file']


class VideoTranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoTranscription
        fields = '__all__'

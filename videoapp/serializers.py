from rest_framework import serializers
from .models import Video, VideoTranscription


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['__all__']


class VideoTranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoTranscription
        fields = '__all__'

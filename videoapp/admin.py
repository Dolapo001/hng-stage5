from django.contrib import admin
from .models import Video, VideoTranscription

# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)


@admin.register(VideoTranscription)
class VideoTranscriptionAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'transcription', 'created_at')
    search_fields = ('video__title', 'transcription')
    list_filter = ('created_at',)

    def video_title(self, obj):
        return obj.video.title
    video_title.short_description = 'Video Title'





from django.urls import path
from . import views

app_name = 'videoapp'

urlpatterns = [
    path('upload/', views.VideoUploadView.as_view(), name='video-upload'),
    path('transcription/', views.VideoTranscriptionView.as_view(), name='video-transcription')
]

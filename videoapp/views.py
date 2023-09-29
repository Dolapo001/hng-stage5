from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Video, VideoTranscription
from .serializers import VideoSerializer, VideoTranscriptionSerializer
from .video_utils import video_to_audio
from .openai_utils import transcribe_audio


class VideoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @staticmethod
    def post(request):
        serializer = VideoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            video_url = serializer.instance.video_file.url

            return Response({"video_url": video_url}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoTranscriptionView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @staticmethod
    def post(request):
        serializer = VideoTranscriptionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            audio_path = 'path_to_temporary_audi_file.wav'
            video_to_audio(serializer.instance.video_file.path, audio_path)

            transcription_text = transcribe_audio(audio_path)

            video_transcription = VideoTranscription(video=serializer.instance, transcription=transcription_text)
            video_transcription.save()

            video_url = serializer.instance.video_file.url

            return Response({"video_url": video_url, "transcription_text": transcription_text},
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






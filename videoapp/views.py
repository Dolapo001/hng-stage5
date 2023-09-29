from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Video, VideoTranscription
from .serializers import VideoSerializer, VideoTranscriptionSerializer


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



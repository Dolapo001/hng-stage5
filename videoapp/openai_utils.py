import openai
from django.conf import settings


def transcribe_audio(audio_path):
    openai.api_key = settings.OPENAI_API_KEY

    with open(audio_path, 'rb') as audio_file:
        response = openai.Transcription.create(
            audio=audio_file,
            engine='whisper',
            language='en',
        )
        transcription_text = response['text']

    return transcription_text

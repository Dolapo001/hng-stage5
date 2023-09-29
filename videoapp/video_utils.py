import subprocess


def video_to_audio(video_path, audio_path):
    command = [
        'ffmpeg',
        '-i', video_path,
        '-q:a', '0',
        '-map', 'a',
        audio_path
    ]

    subprocess.run(command)

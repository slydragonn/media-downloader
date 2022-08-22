from importlib.resources import path
from os import path, remove
from sys import argv

import ffmpeg
from pytube import YouTube


def download_mp4(link: str):
    print('Downloading mp4 file...')
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download('./video/')
    print('Download Complete!!!')

def download_mp3(link: str):
    print('Downloading mp3 file...')
    audio_title = YouTube(link).title
    audio = YouTube(link).streams.filter(only_audio=True).order_by('abr').desc().first()
    audio.download('./audio/')
    audio_path = path.join('./audio', f"{audio_title}.webm")
    print('Converting webm to mp3...')
    (
        ffmpeg
        .input(audio_path)
        .output(path.join('./audio', f"{audio_title}.mp3"))
        .run()
    )
    remove(audio_path)
    print('Download Complete!!!')


def download():
    video_url = argv[1]
    
    if len(argv) > 2:
        file_format = argv[2]
        
        if file_format == 'mp3':
            return download_mp3(video_url)
        elif file_format == 'mp4':
            return download_mp4(video_url)
        else:
            return print('Bad file Format. Only Accept mp3 or mp4 formats!')
    
    download_mp4(video_url)

if __name__ == '__main__':
    download()

from moviepy.editor import *
import pytube 
import os
from pytube.cli import on_progress

def get_sec(time_str):
    """Get seconds from time.
    """

    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def youtube_preprocess(link, start = None, end = None):
    yt = pytube.YouTube(link, on_complete_callback=on_progress)
    destination = '.'
    video = yt.streams.filter(only_audio = True).first()

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)

    new_file = base + '.wav'
    os.rename(out_file, new_file)

    if start and end:
        myclip = AudioFileClip(new_file).subclip(get_sec(start),get_sec(end))
        
        
    return new_file
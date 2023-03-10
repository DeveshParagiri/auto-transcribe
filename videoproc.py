from moviepy.editor import *
import pytube 
import os


def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def youtube_to_audio(link, start = None, end = None):
    yt = pytube.YouTube(link)
    destination = '.'

    video = yt.streams.filter(only_audio = True).first()

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)

    new_file = base + '.wav'
    os.rename(out_file, new_file)

    if start and end:
        myclip = AudioFileClip(new_file).subclip(get_sec(start),get_sec(end))
        myclip.write_audiofile(base+".wav")
        
    return new_file
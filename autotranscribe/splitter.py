from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

def split(path):
    song = AudioSegment.from_file(path)
    audio_chunks = split_on_silence(song, min_silence_len=300, silence_thresh=-40, seek_step = 5000)
    os.mkdir("process_chunks")
    for i,chunk in enumerate(audio_chunks):
        output_file = "process_chunks/chunk{0}.wav".format(i)
        chunk.export(output_file, format="wav")
    return i + 1

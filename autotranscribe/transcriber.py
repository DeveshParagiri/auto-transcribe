import whisper
import time
from datetime import timedelta
from autotranscribe.videoproc import youtube_preprocess
from autotranscribe.advanced import result_multi

def transcribe_from_youtube(url, file_out, start=None, end=None, multiproc=False, extensive=False):
    '''
    Transcribes the given youtube URL to specified file path.

    Parameters:
    url (str): YouTube URL
    file_out (str): Text file destination
    start (str, optional): Timestamp of video subclip
    end (str, optional): Timestamp of video subclip
    multiproc (boolean, optional): Enable multiprocessing for transcription
    extensive (boolean, optional): Loads larger model for higher accuracy and multilingual support
    Returns:
    dict: Information of transcription with file path, duration and nature of model used
    '''

    start_time = time.time()
    model = whisper.load_model('large') if extensive else whisper.load_model('base')

    file_in = youtube_preprocess(url, start, end)

    if multiproc:
        result_multi(file_in, file_out)
    else:
        result = model.transcribe(file_in, fp16 = False)

        with open(file_out,'w') as f:
            f.write(result["text"])
        
    end_time = time.time()

    duration = str(timedelta(seconds=end_time-start_time))

    info = {'video_url': url, 
            'output_path': file_out, 
            'processing_duration': duration,
            'multiprocessing': multiproc,
            'model_large': extensive}
    return info

def transcribe_from_video(file_in, file_out, multiproc=False, extensive=False):
    '''
    Transcribes the given video to specified file path.

    Parameters:
    file_in (str): Video/Audio path
    file_out (str): Text file destination
    multiproc (boolean, optional): Enable multiprocessing for transcription
    extensive (boolean, optional): Loads larger model for higher accuracy and multilingual support

    Returns:
    dict: Information of transcription with file path, duration and nature of model used.
    '''

    start_time = time.time()
    model = whisper.load_model('large') if extensive else whisper.load_model('base')

    if multiproc:
        result_multi(file_in, file_out)
    else:
        result = model.transcribe(file_in, fp16 = False)
        with open(file_out,'w') as f:
            f.write(result["text"])
        
    end_time = time.time()

    duration = str(timedelta(seconds=end_time-start_time))

    info = {'input_path': file_in, 
            'output_path': file_out, 
            'processing_duration': duration,
            'multiprocessing': multiproc,
            'model_large': extensive}
    return info
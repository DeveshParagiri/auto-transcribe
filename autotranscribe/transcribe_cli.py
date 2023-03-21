import whisper
import time
from datetime import timedelta
import os
import argparse
from videoproc import youtube_preprocess
from advanced import result_multi

def transcribe_basic_cli(args):
    start = time.time()

    if args.large:
        model = whisper.load_model("large")
    else:
        model = whisper.load_model("base")

    if args.yttranscribe != None:
        if args.ytclipvideo:
            start_time = args.ytclipvideo[0]
            end_time = args.ytclipvideo[1]
            file_in = youtube_preprocess(args.yttranscribe[0], start_time, end_time)
        else:
            file_in = youtube_preprocess(args.yttranscribe[0])

        file_out = args.yttranscribe[1]
        
    else:
        file_in = args.transcribe[0]
        file_out = args.transcribe[1]
        
    result = model.transcribe(file_in, fp16 = False)

    with open(file_out, "w") as f:
        f.write(result["text"])
        
    end = time.time()
    
    if args.rmvideo:
        os.remove(file_in)
    print("TIME: ", str(timedelta(seconds=end-start)))

def transcribe_advanced_cli(args):
    start = time.time()
    if args.yttranscribe != None:
        if args.ytclipvideo:
            start_time = args.ytclipvideo[0]
            end_time = args.ytclipvideo[1]
            file_in = youtube_preprocess(args.yttranscribe[0], start_time, end_time)
        else:
            file_in = youtube_preprocess(args.yttranscribe[0])

        file_out = args.yttranscribe[1]
    else:
        file_in = args.transcribe[0]
        file_out = args.transcribe[1]

    result_multi(file_in, file_out)

    end = time.time()

    if args.rmvideo:
        os.remove(file_in)
    print("TIME: ", str(timedelta(seconds=end-start)))

def main():

    parser = argparse.ArgumentParser(description = "A transcriber!")

    parser.add_argument("--transcribe", type = str, nargs = 2, metavar = ("audiofile_in", "txtfile_out"), default = None, help = "Transcribes the current audio file to output path file.")

    parser.add_argument("--yttranscribe", type = str, nargs = 2, metavar = ("link_in", "txtfile_out"),default=None, help="Transcribes a youtube video.")

    parser.add_argument("--large", action = "store_true")

    parser.add_argument("--ytclipvideo", type = str, nargs = 2, metavar = ("start_time", "end_time"),default=None, help="Sub clip of a youtube video.")

    parser.add_argument("--multiproc", action = "store_true")

    parser.add_argument("--rmvideo", action = "store_true")
    
    args = parser.parse_args()

    if args.multiproc:
        transcribe_advanced_cli(args)
    else:
        transcribe_basic_cli(args)
    
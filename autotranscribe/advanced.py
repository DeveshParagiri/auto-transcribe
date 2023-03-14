import whisper
from autotranscribe.splitter import split
from datetime import timedelta
import multiprocessing
import psutil
import shutil

model = whisper.load_model("base")


def subproc(path):
    result = model.transcribe(path, fp16=False)
    return result["text"]


def result_multi(file_in, file_out):

    files = split(file_in)
    cpus = psutil.cpu_count(logical=True)
    process = cpus - 2
    if files < process:
        process = files
    
    pool = multiprocessing.Pool(process)
    processes = [pool.apply_async(subproc, args=("process_chunks/chunk{0}.wav".format(x),)) for x in range(files)]

    with open(file_out, "w") as f:
        for p in processes:
            f.write(p.get())
    
    pool.close()
    pool.join()
    shutil.rmtree("process_chunks")
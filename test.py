import whisper

model = whisper.load_model("base")
result = model.transcribe('Welcome.wav',fp16=False)

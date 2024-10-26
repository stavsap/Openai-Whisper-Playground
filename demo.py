import whisper

# whisper has multiple models that you can load as per size and requirements
model = whisper.load_model("large-v3", device="cuda", in_memory=True, download_root="./models")

# path to the audio file you want to transcribe
PATH = "audio.mp3"

result = model.transcribe(PATH)
print("----------------------------------")
print(result["text"])

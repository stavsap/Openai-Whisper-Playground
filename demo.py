import whisper, logging
"""Set up logging configuration"""
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("whisper")

model = "large-v3"
path = "audio.mp3"
output = "output.txt"

logger.info("Starting Whisper Demo with model ["+model+"]")
model = whisper.load_model(model, device="cuda", in_memory=True, download_root="./models")

logger.info("Starting transcribe for [" + path + "]")
result = model.transcribe(path)
logger.info("Completed transcribe for [" + path + "], writing result to: ["+output+"]")

with open(output, "w") as file:
    file.write(result["text"])

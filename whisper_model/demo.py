# import requests

# API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
# headers = {"Authorization": "Bearer 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"}

# def query(filename):
#     with open(filename, "rb") as f:
#         data = f.read()
#     response = requests.post(API_URL, headers=headers, data=data)
#     return response.json()

# output = query(r'C:\Users\darsh\Desktop\Voice Assistant\offline\output.wav')
# print(output)

from transformers import AutoConfig, WhisperForConditionalGeneration
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3"

processor = AutoProcessor.from_pretrained(model_id)
# Load the configuration
config = AutoConfig.from_pretrained(r'C:\Users\darsh\Desktop\Voice Assistant\cache\models--openai--whisper-tiny\snapshots\169d4a4341b33bc18d8881c4b69c2e104e1cc0af\config.json')

# Instantiate the Whisper ASR model using the loaded configuration
model = WhisperForConditionalGeneration(config=config)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)


# Read the audio file
audio_file_path = r'C:\Users\darsh\Desktop\Voice Assistant\offline\output.wav'

# Perform speech recognition
with open(audio_file_path, "rb") as audio_file:
    data = audio_file.read()
response = pipe(data)
tre=response.json()

print(tre.text)




from transformers import WhisperForConditionalGeneration

model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny", cache_dir=r'C:\Users\darsh\Desktop\Voice Assistant\cache')

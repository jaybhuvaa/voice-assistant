import vosk
import wave
from pydub import AudioSegment
import librosa
#C:\Users\darsh\Downloads\harvard (1).wav
model = vosk.Model(r'C:\Users\darsh\Downloads\vosk-model-en-in-0.5\vosk-model-en-in-0.5')  # Replace with your model path
wf = wave.open(r'C:\Users\darsh\Desktop\Voice Assistant\offline\output.wav', mode="rb")
rec = vosk.KaldiRecognizer(model, 16000)  # Sample rate of your audio (adjust if needed)

chunk_size = 4000
data = wf.readframes(chunk_size)

while data:
    if rec.AcceptWaveform(data):
        result = rec.Result()  # Get partial results
        print(result)
    data = wf.readframes(chunk_size)

result = rec.FinalResult()
print(result)

wf.close()

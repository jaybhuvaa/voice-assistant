import whisper
import sounddevice as sd
import wave

def speech_to_text(file_name):
    model = whisper.load_model("base.en")
    result = model.transcribe(file_name, fp16=False)
    return(result["text"])

def record_audio(filename, duration=5, samplerate=44100):
    # Record audio
    audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    # Save audio as WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())

if __name__ == "__main__":
    # Specify the filename for the WAV file
    wav_filename = "output.wav"
    # Record audio for 5 seconds (adjust the duration as needed)
    record_audio(wav_filename, duration=5)
    text=speech_to_text(wav_filename)
    print(text)
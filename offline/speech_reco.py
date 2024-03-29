import sounddevice as sd
import wave
from pydub import AudioSegment
import librosa
import io
import soundfile as sf
#AudioSegment.converter = r'C:\Users\darsh\Downloads\ffmpeg-6.1.1\ffmpeg-6.1.1'


def pre_process_audio( target_sample_rate=16000):
    with wave.open(r'C:\Users\darsh\Desktop\Voice Assistant\offline\output.wav', mode="rb") as wf:
        # Convert Wave_read object to bytes
        audio_bytes = wf.readframes(wf.getnframes())
        
        # Create a seekable file-like object
        audio_file = io.BytesIO(audio_bytes)
        
        # Now you have a valid seekable file-like object you can use with Pydub
        audio = AudioSegment.from_wav(audio_file)
        
        y, sr = librosa.load(audio_file, sr=None)
        cleaned_y = librosa.effects.noise_reduce(y, sr=sr, noise=librosa.effects.get_noise(y, sr)) 
        cleaned_audio = AudioSegment.from_ogg(librosa.output.write_wav(None, cleaned_y, sr))
        cleaned_audio.export("cleaned_audio.wav", format="wav")
        normalized_audio = audio.normalize(normalize_to=-16)  # Adjust dB level as needed
        normalized_audio.export("normalized_audio.wav", format="wav")
        converted_audio = audio.set_frame_rate(16000)
        converted_audio.export("converted_sample_rate.wav", format="wav")

        original_sample_rate = wf.getframerate()

        
        if original_sample_rate != target_sample_rate:
            # Resample the audio using soundfile
            audio_data, _ = sf.read(audio_file)
            resampled_audio = sf.resample(audio_data, original_sample_rate, target_sample_rate)


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
   # record_audio(wav_filename, duration=5)
    pre_process_audio()

    print(f"Audio recorded and saved as {wav_filename}")

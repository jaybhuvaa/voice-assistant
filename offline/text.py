import speech_recognition as sr



import speech_recognition as sr

def offline_speech_recognition(audio_file_path):
    recognizer = sr.Recognizer()

    # Adjust these parameters based on your needs
    # pocketsphinx_params = {
    #     'lm': r'C:\Users\darsh\Downloads\cmusphinx-en-in-8khz-5.2',
    # }

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_sphinx(audio_data)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Error with the offline speech recognition service; {e}")


# Example usage
audio_file_path = r'C:\Users\darsh\Desktop\Voice Assistant\offline\output.wav'
result = offline_speech_recognition(audio_file_path)

if result:
    print("Offline Speech Recognition Result:", result)

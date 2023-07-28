#this code is to check whether exists or pronunced in a given audio

import speech_recognition as sr

# Function to check if a specific word exists in the audio
def check_word_in_audio(audio_path, target_word):
    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)  # Read the entire audio file

    # Use a speech recognition engine to transcribe the audio
    try:
        transcription = r.recognize_google(audio)
        print("Transcription:", transcription)

        if target_word.lower() in transcription.lower():
            print("Target word found in the audio.")
        else:
            print("Target word not found in the audio.")

    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from the speech recognition service; {0}".format(e))

# Example usage
audio_path = '/content/output_file (2).wav'
target_word = 'blind'

check_word_in_audio(audio_path, target_word)

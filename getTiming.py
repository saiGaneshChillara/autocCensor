#this program finds the timing of given word in the given audio file
import speech_recognition as sr
import wave

def find_word_timing(audio_path, target_word):
    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)  # Load the audio file

    transcript = r.recognize_google(audio)  # Perform speech-to-text conversion

    # Find the target word in the transcript
    word_index = transcript.lower().split().index(target_word.lower())

    # Get the sample rate of the audio
    with wave.open(audio_path, 'rb') as audio_file:
        sample_rate = audio_file.getframerate()

    # Calculate the duration of the audio
    audio_duration = len(audio.frame_data) / (audio.sample_width * audio.sample_rate)

    # Calculate the start and end times of the target word
    word_start_time = audio_duration * (word_index / len(transcript.split()))
    word_end_time = audio_duration * ((word_index + 1) / len(transcript.split()))

    # Print the timing information
    print("Target Word:", target_word)
    print("Start Time:", word_start_time, "seconds")
    print("End Time:", word_end_time, "seconds")

# Example usage
audio_path = "/content/output_file (2).wav"
target_word = "blind"

find_word_timing(audio_path, target_word)

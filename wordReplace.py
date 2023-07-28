#this code finds given word in the given audio file and replaces it with another given word
from gtts import gTTS
import os

def replace_word_in_audio(audio_path, target_word, replacement_word, output_path):
    with open(audio_path, "r", encoding="latin-1") as f:
        text = f.read()

    modified_text = text.replace(target_word, replacement_word)

    tts = gTTS(text=modified_text, lang="en")
    tts.save(output_path)

    print("Modified audio generated successfully.")

# Example usage
audio_path = "/content/output_file (2).wav"
target_word = "blind"
replacement_word = "replaced"
output_path = "replaced.wav"

replace_word_in_audio(audio_path, target_word, replacement_word, output_path)

#this mutes the given audio between the given timings
from pydub import AudioSegment

def mute_audio_segment(audio_path, start_time, end_time, output_path):
    audio = AudioSegment.from_file(audio_path, format="wav")

    # Calculate the start and end positions in milliseconds
    start_position = int(start_time * 1000)
    end_position = int(end_time * 1000)

    # Mute the specified segment of audio
    muted_audio = audio[:start_position] + AudioSegment.silent(duration=end_position - start_position) + audio[end_position:]

    # Export the muted audio to a new file
    muted_audio.export(output_path, format="wav")

# Example usage
audio_path = "/content/output_file (2).wav"
start_time = 5.0  # Start time in seconds
end_time = 10.0  # End time in seconds
output_path = "muted_audio.wav"

mute_audio_segment(audio_path, start_time, end_time, output_path)

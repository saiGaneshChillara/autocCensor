#returns the part of the audio between the given timings
from pydub import AudioSegment

def extract_audio_segment(audio_path, start_time, end_time, output_path):
    audio = AudioSegment.from_file(audio_path, format="wav")
    segment = audio[start_time * 1000 : end_time * 1000]  # Extract the desired segment (in milliseconds)
    segment.export(output_path, format="wav")  # Save the segment to a file

# Example usage
audio_path = "/content/output_file (2).wav"
start_time = 18.836842105263155  # Start time in seconds
end_time =   21.97631578947368 # End time in seconds
output_path = "sliceAudioDemo.wav"  # Output file path

extract_audio_segment(audio_path, start_time, end_time, output_path)

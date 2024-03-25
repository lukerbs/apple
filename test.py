from apple.animator import animate
from apple.lipsync import viseme_sequencer, WordViseme
from apple.util import resample_audio
from pprint import pprint

from moviepy.editor import VideoFileClip, AudioFileClip, vfx


# resampled_audio, sr = resample_audio(audio_file="./temp/speech.wav")
# audio_seconds = len(resampled_audio) / 48000
# print(f"New length: {round(audio_seconds, 2)} (seconds)")

text_path = "./.temp/speech.txt"
audio_path = "./.temp/speech.mp3"
video_path = "./out.mp4"
final_video_path = "./final.mp4"

animate(
    audio_file=audio_path,
    txt_file=text_path,
    video_path=video_path,
)

video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)
print(audio_clip.duration)
audio_clip = audio_clip.set_start(0.3)
video_clip = video_clip.set_audio(audio_clip)
video_clip.write_videofile(final_video_path, codec="libx264", audio_codec="aac")

# Close clips
video_clip.close()
audio_clip.close()
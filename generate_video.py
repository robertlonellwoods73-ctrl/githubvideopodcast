import subprocess
import json

cfg = json.load(open("config.json"))

cmd = [
    "ffmpeg",
    "-loop", "1",
    "-i", cfg["background"],
    "-i", "output/voice.wav",
    "-vf", f"subtitles=output/subtitles.srt:force_style='FontName={cfg['font']}'",
    "-c:v", "libx264",
    "-c:a", "aac",
    "-shortest",
    "output/final.mp4"
]

subprocess.run(cmd)

print("✓ Final video created → output/final.mp4")

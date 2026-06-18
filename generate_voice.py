import subprocess
from pathlib import Path

script = Path("output/script.txt").read_text()
Path("output/script_raw.txt").write_text(script)

subprocess.run([
    "piper",
    "--model", "en_US-ryan-high.onnx",
    "--output_file", "output/voice.wav"
], input=script.encode())

print("✓ Voice generated → output/voice.wav")

from pathlib import Path

script = Path("output/script.txt").read_text().split()
lines = []
start = 0

for i, word in enumerate(script):
    end = start + 1
    lines.append(
        f"{i+1}\n00:00:{start:02d},000 --> 00:00:{end:02d},000\n{word}\n"
    )
    start += 1

Path("output/subtitles.srt").write_text("\n".join(lines))

print("✓ Subtitles generated → output/subtitles.srt")

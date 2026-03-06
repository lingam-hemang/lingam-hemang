import shutil
import os

THEMES = [
    ("themes/netflix.md",  "🎬 Netflix"),
    ("themes/spotify.md",  "🎵 Spotify"),
    ("themes/apple.md",    "🍎 Apple"),
    ("themes/aws.md",      "☁️  AWS"),
]

INDEX_FILE = ".current_theme"

# Read last used index
try:
    with open(INDEX_FILE, "r") as f:
        current = int(f.read().strip())
except (FileNotFoundError, ValueError):
    current = -1

# Advance to next theme (sequential rotation)
next_index = (current + 1) % len(THEMES)
theme_path, theme_name = THEMES[next_index]

# Apply theme
shutil.copy(theme_path, "README.md")

# Persist index
with open(INDEX_FILE, "w") as f:
    f.write(str(next_index))

print(f"✅ Rotated to theme {next_index + 1}/{len(THEMES)}: {theme_name}")

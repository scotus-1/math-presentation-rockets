import os
import re

# Folder containing your media files
MEDIA_DIR = "assets/gracie"

VIDEO_EXTS = {".mp4", ".webm", ".mov", ".mkv"}
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

def numeric_key(filename):
    """Extract leading integer for correct sorting order."""
    match = re.match(r"(\d+)", filename)
    return int(match.group(1)) if match else float("inf")

def generate_section(filename):
    """Return Reveal.js <section> tag for the media file."""
    ext = os.path.splitext(filename)[1].lower()
    path = os.path.join(MEDIA_DIR, filename).replace("\\", "/")

    if ext in VIDEO_EXTS:
        return f'<section data-background-size="contain"  data-background-color="white" data-background-video="{path}" data-background-video-muted="true"></section>'
    elif ext in IMAGE_EXTS:
        return f'<section data-background-image="{path}"></section>'
    else:
        return None

def main():
    files = sorted(
        [f for f in os.listdir(MEDIA_DIR) if os.path.isfile(os.path.join(MEDIA_DIR, f))],
        key=numeric_key
    )

    for f in files:
        section = generate_section(f)
        if section:
            print(section)

if __name__ == "__main__":
    main()

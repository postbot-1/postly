import subprocess
import os
import shutil


def ffmpeg_exists():
    return shutil.which("ffmpeg") is not None


def convert_to_instagram_format(filepath):
    ext = filepath.lower().split('.')[-1]

    # If ffmpeg not available (local), skip conversion
    if not ffmpeg_exists():
        print("⚠️ FFmpeg not found — skipping conversion (local mode)")
        return filepath

    output_path = filepath

    # VIDEO CONVERSION
    if ext in ["mov", "avi", "mkv"]:
        output_path = filepath.rsplit('.', 1)[0] + "_ig.mp4"

        subprocess.run([
            "ffmpeg",
            "-i", filepath,
            "-vcodec", "libx264",
            "-acodec", "aac",
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            output_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # IMAGE CONVERSION
    elif ext in ["png", "heic"]:
        output_path = filepath.rsplit('.', 1)[0] + "_ig.jpg"

        subprocess.run([
            "ffmpeg",
            "-i", filepath,
            output_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return output_path

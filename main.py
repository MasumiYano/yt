import os.path
import sys
import argparse
from pytube import YouTube
from pytube.cli import on_progress


def download_video(url: str, file_type: str) -> None:
    yt: YouTube = YouTube(url, on_progress_callback=on_progress)

    if file_type == 'mp4':
        stream = yt.streams.get_highest_resolution()
    elif file_type == 'mp3':
        stream = yt.streams.filter(only_audio=True).first()
    else:
        print("Invalid file type. Choose 'mp3' or 'mp4'.")
        sys.exit(1)

    print(f"Downloading {yt.title}...")
    file_path = stream.download()

    if file_type == 'mp3':
        base, ext = os.path.splitext(file_path)
        new_file = base + '.mp3'
        os.rename(file_path, new_file)
        file_path = new_file

    print(f"Download completed: {file_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download YouTube videos as MP3 or MP4.')
    parser.add_argument("--url", help='YouTube video URL', required=True)
    parser.add_argument("--type", help="File type to download (mp3 or mp4)", choices=['mp3', 'mp4'], required=True)

    args = parser.parse_args()

    download_video(args.url, args.type)

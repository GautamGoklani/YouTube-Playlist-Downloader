from pytube import Playlist
import os

def download_playlist(playlist_url, output_path):
    playlist = Playlist(playlist_url)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for video in playlist.videos:
        print(f"Downloading: {video.title}")
        video.streams.get_highest_resolution().download(output_path)

    print("Playlist download completed.")

if __name__ == "__main__":
    playlist_url = "link of the youtube playlist"
    output_path = r"output path where files are to be stored"

    download_playlist(playlist_url, output_path)
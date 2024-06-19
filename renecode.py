import glob
import os
import shutil
import shlex
import traceback
import av
from tqdm import tqdm

landscape_bitrates = {
    "144p": 150,
    "240p": 350,
    "360p": 750,
    "480p": 1250,
    "720p": 2000,
    "1080p": 5000,
    "2160p (4K)": 12500
}
portrait_bitrates = {
    "144p": 100,
    "240p": 250,
    "360p": 500,
    "480p": 1000,
    "720p": 1500,
    "1080p": 4000,
    "2160p (4K)": 10000
}


def get_video_bitrate(file_path):
    # Open the video file
    try:
        with av.open(file_path) as container:
            total_bitrate = 0
            # Loop through the streams and get the bitrate
            for stream in container.streams:
                if stream.type == 'video':
                    total_bitrate += stream.bit_rate
            total_bitrate = total_bitrate / 1000
            return total_bitrate
    except Exception as e:
        print(f"Error getting bitrate for {file_path}: {e}")
        return 100000


def get_video_dimensions(video_path):
    container = av.open(video_path)
    video_stream = next((stream for stream in container.streams if stream.type == 'video'), None)
    if video_stream is None:
        return None
    else:
        width = video_stream.codec_context.width
        height = video_stream.codec_context.height
        container.close()
        return (width, height)


def move_file(source_path, destination_path):
    """
    Move the file to the destination directory if it does not exist there.
    """
    if not os.path.exists(destination_path):
        shutil.move(source_path, destination_path)


def get_sorted_file_list(directory):
    files_with_sizes = []

    # Walk through directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                files_with_sizes.append((file_path, file_size))
            except OSError as e:
                print(f"Error retrieving size for {file_path}: {e}")

    # Sort files by size in descending order
    sorted_files = sorted(files_with_sizes, key=lambda x: x[1], reverse=True)

    return sorted_files


def process_videos(source_directory, destination_directory):
    """
    Process all video files in the source directory: re-encode and move them to the destination directory.
    """
    video_files = get_sorted_file_list(source_directory)
    for filename in tqdm([x[0] for x in video_files]):
        try:
            width, height = get_video_dimensions(os.path.join(source_directory, filename))
            if width > height:
                if width < 144:
                    bitrate = landscape_bitrates["144p"]
                elif width < 240:
                    bitrate = landscape_bitrates["240p"]
                elif width < 360:
                    bitrate = landscape_bitrates["360p"]
                elif width < 480:
                    bitrate = landscape_bitrates["480p"]
                elif width < 720:
                    bitrate = landscape_bitrates["720p"]
                elif width < 1080:
                    bitrate = landscape_bitrates["1080p"]
                else:
                    bitrate = landscape_bitrates["2160p (4K)"]
            else:
                if height < 144:
                    bitrate = portrait_bitrates["144p"]
                elif height < 240:
                    bitrate = portrait_bitrates["240p"]
                elif height < 360:
                    bitrate = portrait_bitrates["360p"]
                elif height < 480:
                    bitrate = portrait_bitrates["480p"]
                elif height < 720:
                    bitrate = portrait_bitrates["720p"]
                elif height < 1080:
                    bitrate = portrait_bitrates["1080p"]
                else:
                    bitrate = portrait_bitrates["2160p (4K)"]
            print(width, height, bitrate)
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory,
                                            ".".join(os.path.basename(filename).split(".")[:-1]) + ".mp4")
            real_bitrate = get_video_bitrate(source_path)
            if bitrate > real_bitrate:
                bitrate = real_bitrate
            arg_sys = f'ffmpeg -i "{source_path}" -threads 8 -b:v {bitrate}k -c:v hevc_nvenc -preset fast  -c:a aac  -movflags +faststart "{destination_path}" -n'
            print(arg_sys)
            os.system(arg_sys)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print("Re-encoding and moving completed.")


if __name__ == "__main__":
    process_videos(r"E:\final_file\error", r"E:\final_file\reencode")

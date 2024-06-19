import os
import random
import subprocess

import tqdm
from moviepy.editor import VideoFileClip
import av


def get_video_resolution(filepath):
    try:
        clip = VideoFileClip(filepath)
        width, height = clip.size
        clip.close()
        return (width, height)
    except Exception as e:
        print(f"Error getting resolution for {filepath}: {e}")
        return None


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


def sort_directory(dirname):
    bar = tqdm.tqdm()
    for root, dirs, files in os.walk(dirname):
        for file in files:
            try:
                bar.update(1)
                dimension = get_video_dimensions(os.path.join(root, file))
                if dimension:
                    width, height = dimension
                    print(width, height)

                    if width > height:
                        if width < 144:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\landscape", "144p", file))
                        elif width < 240:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\landscape", "240p", file))
                        elif width < 360:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\landscape", "360p", file))
                        elif width < 480:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\landscape", "480p", file))
                        elif width < 720:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\landscape", "720p", file))
                        elif width < 1080:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\landscape", "1080p", file))
                        else:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\landscape", "2160p", file))
                    else:
                        if height < 144:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\portrait", "144p", file))
                        elif height < 240:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\portrait", "240p", file))
                        elif height < 360:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\portrait", "360p", file))
                        elif height < 480:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\portrait", "480p", file))
                        elif height < 720:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\portrait", "720p", file))
                        elif height < 1080:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\portrait", "1080p", file))
                        else:
                            os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\portrait", "2160p", file))
                else:
                    raise ValueError(f"Failed to get video dimensions for {file}")
            except Exception as e:
                print(e)
                try:
                    os.rename(os.path.join(root, file), os.path.join(r"E:\final_file\error", file))
                    print(f"Error processing {file}: {e}")
                except:
                    continue


sort_directory(r"E:\final_file\all")

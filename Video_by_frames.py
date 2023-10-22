import numpy as np
import os
import time
from datetime import datetime, date, time, timedelta

from moviepy.editor import VideoFileClip
# кол-во фреймов
SAVING_FRAMES_PER_SECONDS = 1

def format_timedelta(td):
    result = str(td)
    try:
        result,ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":","-")
    ms = round((int(ms) / 10000))
    return f"{result}.{ms:02}".replace(":","-")

def main(video_file):
    video_clip = VideoFileClip(video_file)
    filename,_ = os.path.splitext(video_file)
    if not os.path.isdir(filename):
        os.mkdir(filename)
    saving_frames_per_second = min(video_clip.fps,SAVING_FRAMES_PER_SECONDS)
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
    for current_duration in np.arange(0,video_clip.duration,step):
        frame_duration_formatted = format_timedelta(timedelta(seconds = current_duration)).replace(":","-")
        frame_filename = os.path.join(filename,f"frame{frame_duration_formatted}.png")
        line = str(frame_filename)[5::]
        print(line)
        video_clip.save_frame(frame_filename,current_duration)

#название видео файла
video_file = "test.mp4"
main(video_file)

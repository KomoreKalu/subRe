#!/usr/bin/python3
import os
import sys

video_ext = "mkv"
sub_ext = "ass"
folder = os.getcwd()
video_name = []
sub_name = []


def get_name(path):
    global video_ext, sub_ext
    for file in os.listdir(path):
        if os.path.isfile(file) and video_ext == os.path.splitext(file)[-1][1:]:
            video_name.append(os.path.splitext(file)[0])
        if os.path.isfile(file) and sub_ext == os.path.splitext(file)[-1][1:]:
            sub_name.append(file)
    if len(video_name) != len(sub_name):
        print("file amount(video&subtitle) doesn't match")
        exit(1)
    video_name.sort()
    sub_name.sort()


def rename():
    global video_name, sub_name
    for i in range(len(video_name)):
        os.rename(sub_name[i], video_name[i] + "." + sub_ext)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        video_ext = sys.argv[1]
        sub_ext = sys.argv[2]
    get_name(folder)
    rename()

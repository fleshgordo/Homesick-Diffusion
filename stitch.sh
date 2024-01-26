#!/bin/bash

#find video -name "*-frame.mp4" -execdir basename {} \; | sort | xargs -I {} echo "file '{}'" > video/file_list.txt

# stitch images 1 frame per second into one video file
#ffmpeg -framerate 1 -pattern_type glob -i 'output_sdxl/output_*.png' -c:v libx264 -r 30 -pix_fmt yuv420p output_hardcut.mp4

# extract audio
#ffmpeg -i bobdylan.mp4 -vn -acodec copy output_audio.aac

# merge audio and video
ffmpeg -i output_sdxl/output.mp4 -i output_audio.aac -c:v copy -c:a aac -strict experimental output_merged.mp4
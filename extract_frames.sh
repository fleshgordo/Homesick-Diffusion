#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 video-file.mp*"
    echo "Please provide a video (mp4) file."
    exit 1
fi

mkdir -p output
mkdir -p output_sdxl
ffmpeg -i $1 -vf fps=1 output/output_%03d.png
# Subterranean Homesick Diffusion

This project is an experiment into the latent space of diffusion models  to see what happens if you create various feedback loops with generic generative image and classification tools. It visualises what the model "sees"
and plays with the ambiguity of reading between the lines. Starting point is the music clip
by [Bob Dylan Subterranean Homesick Blues](https://www.youtube.com/watch?v=MGxjIBEZvx0). The individual frames are interpreted by an img2prompt model and the generated prompts are being fed back into a stable diffusion prompt. 

Get the mp4 file via [youtube-dl](https://github.com/yt-dlp/yt-dlp) if you want to re-create this experiment.

[![Watch the video](https://i.vimeocdn.com/video/1788725174-fe30f52a68845c0922b6192f86d130bb8381f0366395f022c44717b6fd9c3976-d?mw=1100&mh=825&q=70)](https://vimeo.com/906760283)

[Play the audio](https://www.youtube.com/watch?v=1I_oWQmddMk)

The generated video is [available here](https://vimeo.com/906760283) (due to copyright issues it's without sound. Make sure you start the [audio clip](https://www.youtube.com/watch?v=1I_oWQmddMk) at the same time as the online video)

## Installation

You need a terminal, python3, replicate module and ffmpeg installed.

```
pip install replicate
```

## Step 1: extracting still image frames (1 frame per sec.) from video

```bash
./extract_frames.sh bobdylan.mp4
```

## Step 2: Analyse still images with img2 model

You'll need to export your REPLICATE API key in your terminal environment. Otherwise the following scripts won't work

```bash
export REPLICATE_API_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

This [img2prompt model](https://replicate.com/methexis-inc/img2prompt) will analyse each frame and generate prompts for stable diffusion in a csv file ```prompts.csv``` "filename, prompt"

```bash
python generate_prompts.py
```

## Step 3: Generate images based on the prompts with stable diffusion model

This will parse the prompts.csv and will send them to [stable diffusion model](https://replicate.com/stability-ai/sdxl)

```bash
python generate_images.py
```

## Step 4 Stitch frames back together

Take frames and stitch them back to video

```bash
ffmpeg -framerate 1 -pattern_type glob -i 'output_sdxl/output_*.png' -c:v libx264 -r 30 -pix_fmt yuv420p output_hardcut.mp4
```

In case you have the audio file merge video and audio with

```bash
# merge audio and video
ffmpeg -i output_hardcut -i output_audio.aac -c:v copy -c:a aac -strict experimental merged.mp4
```

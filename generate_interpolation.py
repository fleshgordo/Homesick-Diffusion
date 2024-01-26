import replicate
import os, csv
import requests
from urllib.parse import urlparse
import itertools

output_csv = "prompts.csv"
input_folder = "output"
generate_folder = "output_sdxl"
video_folder = "video"

def generate_frame_interpolation():
    files = [file for file in sorted(os.listdir(generate_folder)) if file.endswith(".png")]
    for i in range(0, len(files)):
        if (i != len(files) -1 ):
            frame1 = files[i]
            frame2 = files[i+1]

            print(f"🎬 sending file1: {files[i]} file2: {files[i+1]} to model for frame interpolation")
            
            output = replicate.run(
            "google-research/frame-interpolation:4f88a16a13673a8b589c18866e540556170a5bcb2ccdc12de556e800e9456d3d",
            input={
                "frame1": open(f"{generate_folder}/{frame1}", "rb"),
                "frame2": open(f"{generate_folder}/{frame2}", "rb"),
                "times_to_interpolate": 4
            }
            )
            response = requests.get(output)
            filename = "%03d-frame.mp4" % i
            save_path = os.path.join(video_folder, filename)
            if response.status_code == 200:
                with open(f"{save_path}", 'wb') as file:
                    file.write(response.content)
                    print(f"fetching file from {output} and saving to {save_path}")  
    print("🏁 done")

generate_frame_interpolation()
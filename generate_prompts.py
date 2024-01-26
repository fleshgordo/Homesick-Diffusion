import replicate
import os, csv
import requests
from urllib.parse import urlparse
import itertools

output_csv = "prompts.csv"
input_folder = "output"
generate_folder = "output_sdxl"
video_folder = "video"

def generate_prompts():
    # Create csv file with headers
    with open(output_csv, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["filename", "prompt"])
    # Iterate images
    for png_file in sorted(os.listdir(input_folder)):
        if png_file.endswith(".png"):
            # Call img2prompt 
            output = replicate.run(
                "methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5",
                input={ "image" : open(f"{input_folder}/{png_file}", "rb")
                }
            )
            output = output.replace("\n", "")
            print(f"** processing {png_file}, generating prompt \"{output}\"")
            with open(output_csv, "a", newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([png_file, output])

    print(f"CSV file '{output_csv}' created successfully.")

generate_prompts()
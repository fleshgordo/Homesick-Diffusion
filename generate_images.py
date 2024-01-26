import replicate
import os, csv
import requests
from urllib.parse import urlparse
import itertools

output_csv = "prompts.csv"
input_folder = "output"
generate_folder = "output_sdxl"
video_folder = "video"

def generate_images(start_offset=1):
    with open(output_csv, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for _ in itertools.islice(csv_reader, start_offset - 1):
            pass
        # Iterate over each row
        for row in csv_reader:
            filename = row["filename"]
            prompt = row["prompt"]
            output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={
                "width": 1024,
                "height": 768,
                "prompt": prompt,
                "refine": "expert_ensemble_refiner",
                "scheduler": "K_EULER",
                "lora_scale": 0.6,
                "num_outputs": 1,
                "guidance_scale": 7.5,
                "apply_watermark": False,
                "high_noise_frac": 0.8,
                "negative_prompt": "",
                "prompt_strength": 0.8,
                "num_inference_steps": 25
            }
            )
            url = output[0]
            response = requests.get(url)
            save_path = os.path.join(generate_folder, filename)
            if response.status_code == 200:
                with open(f"{save_path}", 'wb') as file:
                    file.write(response.content)
            print(f"return url from model: {url} -> saving to: {save_path}, Prompt: {prompt}")

generate_images()
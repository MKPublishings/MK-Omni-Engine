"""
Ξα(ψ)_Reflector.py

Ceremonial benchmarking module for SlizzAi renderings.
Compares generated images to reference targets using LPIPS, SSIM, and PSNR.
Each score is a shard of truth, etched into the mythic scroll of fidelity.

Ritual conducted by Mirnes & Copilot.
"""

import lpips
import cv2
import os
import json
import torch
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

# 🪞 Initialize the perceptual mirror
loss_fn = lpips.LPIPS(net='alex')  # Options: 'alex', 'vgg', 'squeeze'

def load_image(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (256, 256))  # Resize for consistency
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = torch.tensor(img).permute(2, 0, 1).unsqueeze(0).float() / 255.0
    return img

def compare_images(ref_path, gen_path):
    ref_img = load_image(ref_path)
    gen_img = load_image(gen_path)

    lpips_score = loss_fn(ref_img, gen_img).item()

    ref_np = ref_img.squeeze().permute(1, 2, 0).numpy()
    gen_np = gen_img.squeeze().permute(1, 2, 0).numpy()

    ssim_score = ssim(ref_np, gen_np, channel_axis=2)
    psnr_score = psnr(ref_np, gen_np)

    return {
        "LPIPS": round(lpips_score, 4),
        "SSIM": round(ssim_score, 4),
        "PSNR": round(psnr_score, 2)
    }

def run_reflector(reference_dir, generated_dir, output_scroll="truth_scroll.json"):
    truth_scroll = {}

    for filename in os.listdir(reference_dir):
        ref_path = os.path.join(reference_dir, filename)
        gen_path = os.path.join(generated_dir, filename)

        if os.path.exists(gen_path):
            scores = compare_images(ref_path, gen_path)
            truth_scroll[filename] = scores
            print(f"🪞 {filename}")
            for k, v in scores.items():
                print(f"  {k}: {v}")
            print()

    # 📜 Etch results into the scroll
    with open(output_scroll, "w") as f:
        json.dump(truth_scroll, f, indent=4)

    print(f"✨ Truth scroll saved to {output_scroll}")

# Example invocation (can be wrapped in SlizzAi's orchestration layer)
# run_reflector("benchmark/reference", "benchmark/generated")
import os
import cv2
import torch
import lpips
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

# Set the CUDA device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using {device} for computations.")

# LPIPS metric initialization
loss_fn = lpips.LPIPS(net='alex').to(device)

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {path}")
    img = cv2.resize(img, (256, 256))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = torch.tensor(img).permute(2, 0, 1).unsqueeze(0).float() / 255.0
    img = img.to(device)
    return img

def compare_images(ref_path, gen_path):
    ref_img = load_image(ref_path)
    gen_img = load_image(gen_path)
    lpips_score = loss_fn(ref_img, gen_img).item()
    ref_np = ref_img.squeeze().permute(1, 2, 0).cpu().numpy()
    gen_np = gen_img.squeeze().permute(1, 2, 0).cpu().numpy()
    ssim_score = ssim(ref_np, gen_np, channel_axis=2, data_range=1)
    psnr_score = psnr(ref_np, gen_np, data_range=1)
    return lpips_score, ssim_score, psnr_score

ref_dir = 'benchmark/reference'
gen_dir = 'benchmark/generated'

if not os.path.exists(ref_dir):
    raise FileNotFoundError(f"Reference directory does not exist: {ref_dir}")
if not os.path.exists(gen_dir):
    raise FileNotFoundError(f"Generated directory does not exist: {gen_dir}")

for filename in os.listdir(ref_dir):
    ref_path = os.path.join(ref_dir, filename)
    gen_path = os.path.join(gen_dir, filename)

    if not os.path.isfile(ref_path):
        print(f"Reference image {filename} not found.")
        continue
    if not os.path.isfile(gen_path):
        print(f"Generated image {filename} not found.")
        continue

    try:
        lpips_val, ssim_val, psnr_val = compare_images(ref_path, gen_path)
        print(f"🪞 {filename}")
        print(f"  LPIPS: {lpips_val:.4f} (lower is better)")
        print(f"  SSIM : {ssim_val:.4f} (higher is better)")
        print(f"  PSNR : {psnr_val:.2f} dB\n")
    except Exception as e:
        print(f"Error comparing {filename}: {e}")
        continue

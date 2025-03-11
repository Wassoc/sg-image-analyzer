# from pidng.core import RPICAM2DNG, DNGTags, Tag
# from pidng.camdefs import *
import numpy as np
import rawpy
import sys
import os

BLACK_LEVEL = 256
MIN_VALUE = 260

red_mins = []
red_maxs = []
red_means = []
red_stds = []

blue_mins = []
blue_maxs = []
blue_means = []
blue_stds = [] 

green_b_mins = []
green_b_maxs = []
green_b_means = []
green_b_stds = []

green_r_mins = []
green_r_maxs = []
green_r_means = []
green_r_stds = []


if len(sys.argv) < 2:
    print("Please provide a parent directory of the DNG files as argument")
    sys.exit(1)

dng_parent_dir = os.path.join("C:/Users/MatthewGreen/Pictures/diffuser-test", sys.argv[1])
for i in range(1, 8):
    dng_file = os.path.join(dng_parent_dir, f"test-{i}-32.dng")
    raw = rawpy.imread(dng_file)

    # Get raw data as numpy array
    raw_data = np.clip(raw.raw_image, BLACK_LEVEL, 4096)
    masked_raw_data = raw_data[raw_data > MIN_VALUE]
    red_pixels = raw_data[1::2, 1::2]
    blue_pixels = raw_data[::2, ::2]
    green_b_pixels = raw_data[::2, 1::2]
    green_r_pixels = raw_data[1::2, ::2]
    
    red_mins.append(np.min(red_pixels[red_pixels > MIN_VALUE]))
    red_maxs.append(np.max(red_pixels[red_pixels > MIN_VALUE]))
    red_means.append(np.mean(red_pixels[red_pixels > MIN_VALUE]))
    red_stds.append(np.std(red_pixels[red_pixels > MIN_VALUE]))

    blue_mins.append(np.min(blue_pixels[blue_pixels > MIN_VALUE]))
    blue_maxs.append(np.max(blue_pixels[blue_pixels > MIN_VALUE]))
    blue_means.append(np.mean(blue_pixels[blue_pixels > MIN_VALUE]))
    blue_stds.append(np.std(blue_pixels[blue_pixels > MIN_VALUE]))

    green_r_mins.append(np.min(green_r_pixels[green_r_pixels > MIN_VALUE]))
    green_r_maxs.append(np.max(green_r_pixels[green_r_pixels > MIN_VALUE]))
    green_r_means.append(np.mean(green_r_pixels[green_r_pixels > MIN_VALUE]))
    green_r_stds.append(np.std(green_r_pixels[green_r_pixels > MIN_VALUE]))

    green_b_mins.append(np.min(green_b_pixels[green_b_pixels > MIN_VALUE]))
    green_b_maxs.append(np.max(green_b_pixels[green_b_pixels > MIN_VALUE]))
    green_b_means.append(np.mean(green_b_pixels[green_b_pixels > MIN_VALUE]))
    green_b_stds.append(np.std(green_b_pixels[green_b_pixels > MIN_VALUE]))
    raw.close()

print("Red Min,," + ",".join([f"{x:.3f}" for x in red_mins]))
print("Red Max,," + ",".join([f"{x:.3f}" for x in red_maxs]))
print("Red Mean,," + ",".join([f"{x:.3f}" for x in red_means]))
print("Red Std,," + ",".join([f"{x:.3f}" for x in red_stds]))
print("")
print("GR Min,," + ",".join([f"{x:.3f}" for x in green_r_mins]))
print("GR Max,," + ",".join([f"{x:.3f}" for x in green_r_maxs]))
print("GR Mean,," + ",".join([f"{x:.3f}" for x in green_r_means]))
print("GR Std,," + ",".join([f"{x:.3f}" for x in green_r_stds]))
print("")
print("GB Min,," + ",".join([f"{x:.3f}" for x in green_b_mins]))
print("GB Max,," + ",".join([f"{x:.3f}" for x in green_b_maxs]))
print("GB Mean,," + ",".join([f"{x:.3f}" for x in green_b_means]))
print("GB Std,," + ",".join([f"{x:.3f}" for x in green_b_stds]))
print("")
print("Blue Min,," + ",".join([f"{x:.3f}" for x in blue_mins]))
print("Blue Max,," + ",".join([f"{x:.3f}" for x in blue_maxs]))
print("Blue Mean,," + ",".join([f"{x:.3f}" for x in blue_means]))
print("Blue Std,," + ",".join([f"{x:.3f}" for x in blue_stds]))

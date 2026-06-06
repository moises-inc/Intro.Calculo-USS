from PIL import Image
import numpy as np
import os

def analyze_shapes(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return
    img = Image.open(filename).convert('RGB')
    arr = np.array(img)
    h, w, c = arr.shape
    print(f"=== {filename} ({w}x{h}) ===")
    
    # Check for text or label colors
    # Blue: RGB (0, 32, 91) is USSBlue, but let's look for saturated blue:
    sat_blue = (arr[:,:,2] > 200) & (arr[:,:,0] < 50) & (arr[:,:,1] < 50)
    # Green:
    sat_green = (arr[:,:,1] > 200) & (arr[:,:,0] < 50) & (arr[:,:,2] < 50)
    # Red:
    sat_red = (arr[:,:,0] > 200) & (arr[:,:,1] < 50) & (arr[:,:,2] < 50)
    
    print(f"Saturated Blue pixels: {sat_blue.sum()}")
    print(f"Saturated Green pixels: {sat_green.sum()}")
    print(f"Saturated Red pixels: {sat_red.sum()}")
    
    # Check for grid lines (usually gray, like 220, 220, 220 or 240, 240, 240)
    gray = (arr[:,:,0] == arr[:,:,1]) & (arr[:,:,1] == arr[:,:,2]) & (arr[:,:,0] > 200) & (arr[:,:,0] < 240)
    print(f"Gray grid pixels: {gray.sum()}")

analyze_shapes('Presentación/image2.png')
analyze_shapes('Presentación/image5.png')
analyze_shapes('Presentación/image8.png')
analyze_shapes('Presentación/image9.png')
analyze_shapes('Presentación/image13.png')

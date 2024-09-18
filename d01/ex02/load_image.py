from PIL import Image
import numpy as np

def ft_load(path: str):
    try:
        img = Image.open(path).convert('RGB')
    except Exception as e:
        print(str(e))
        return None

    pixels = np.array(img)

    print(f"The shape of the image is {pixels.shape[:3]}")

    return pixels

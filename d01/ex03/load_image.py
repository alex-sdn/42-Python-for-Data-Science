from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads the image at the given path and prints its format.
    Returns the pixels content in RGB as a numpy.ndarray.
    """
    try:
        img = Image.open(path).convert('RGB')
    except Exception as e:
        print(str(e))
        return None

    pixels = np.array(img)

    print(f"The shape of the image is {pixels.shape}")

    return pixels

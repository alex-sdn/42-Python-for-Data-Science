from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pixels = ft_load("animal.jpeg")
    print(pixels)

    if pixels is not None:
        zoomed_pixels = pixels[200:600, 400:800]
        rotated_pixels = np.rot90(zoomed_pixels)

        print(f"New shape after transpose is {rotated_pixels.shape[:3]}")
        print(rotated_pixels)

        plt.imshow(rotated_pixels)
        plt.show()

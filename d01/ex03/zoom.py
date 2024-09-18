from load_image import ft_load
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pixels = ft_load("animal.jpeg")
    print(pixels)

    if pixels is not None:
        # not b&w ?
        zoomed_pixels = pixels[200:600, 400:800]
        
        print(f"New shape after slicing is {zoomed_pixels.shape[:3]}")
        print(zoomed_pixels)

        plt.imshow(zoomed_pixels)
        plt.show()

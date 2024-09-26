from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """Loads animal.jpeg, zooms in and displays the new image"""
    pixels = ft_load("animal.jpeg")
    print(pixels)

    if pixels is not None:
        zoomed_pixels = pixels[150:550, 450:850]

        print(f"New shape after slicing is {zoomed_pixels.shape}")
        print(zoomed_pixels)

        plt.imshow(zoomed_pixels)
        plt.show()


if __name__ == '__main__':
    main()

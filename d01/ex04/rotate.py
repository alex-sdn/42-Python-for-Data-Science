from load_image import ft_load
import matplotlib.pyplot as plt


def rotate(pixels):
    """Rotates a numpy array by 90 degree"""
    rot_pixels = pixels.copy()
    size = len(pixels)

    try:
        for i in range(size):
            for j in range(size):
                rot_pixels[j][i] = pixels[i][j]

        return rot_pixels
    except Exception as e:
        print(str(e))
        return pixels


def main():
    """Loads the img, resizes and rotates it before displaying"""
    pixels = ft_load("animal.jpeg")
    pixels = pixels[:, :, 0]
    print(pixels)

    if pixels is not None:
        zoomed_pixels = pixels[100:500, 400:800]
        rotated_pixels = rotate(zoomed_pixels)

        print(f"New shape after transpose is {rotated_pixels.shape}")
        print(rotated_pixels)

        plt.imshow(rotated_pixels, cmap='gray')
        plt.show()


if __name__ == '__main__':
    main()

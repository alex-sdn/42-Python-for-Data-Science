import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted = 255 - array

    plt.imshow(inverted)
    plt.show()
    return inverted


def ft_red(array) -> np.ndarray:
    """Keeps only the Red channel of the image received."""
    red = array.copy()
    red[..., [1, 2]] = 0

    plt.imshow(red)
    plt.show()
    return red


def ft_green(array) -> np.ndarray:
    """Keeps only the Green channel of the image received."""
    green = array.copy()
    green[..., [0, 2]] = 0

    plt.imshow(green)
    plt.show()
    return green


def ft_blue(array) -> np.ndarray:
    """Keeps only the Blue channel of the image received."""
    blue = array.copy()
    blue[..., [0, 1]] = 0

    plt.imshow(blue)
    plt.show()
    return blue


def ft_grey(array) -> np.ndarray:
    """Turns the image received to greyscale."""
    grey = array.copy().astype(float)

    grey[..., 0] /= 3
    grey[..., 1] /= 3
    grey[..., 2] /= 3

    grey = grey.astype(np.uint8).sum(axis=-1)
    grey = np.stack([grey, grey, grey], axis=2)

    plt.imshow(grey)
    plt.show()
    return grey

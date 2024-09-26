import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """Inverts the color of the image received."""
    return 255 - array


def ft_red(array):
    """Keeps only the Red channel of the image received."""
    array[..., [1, 2]] = 0
    return array


def ft_green(array):
    """Keeps only the Green channel of the image received."""
    array[..., [0, 2]] = 0
    return array


def ft_blue(array):
    """Keeps only the Blue channel of the image received."""
    array[..., [0, 1]] = 0
    return array


def ft_grey(array):
    """Turns the image received to greyscale."""
    array = array.astype(float)

    array[..., 0] /= 3
    array[..., 1] /= 3
    array[..., 2] /= 3

    grey = array.astype(np.uint8).sum(axis=-1)
    return np.stack([grey, grey, grey], axis=2)

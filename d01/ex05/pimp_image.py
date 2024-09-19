import numpy as np


def ft_invert(array):
    return 255 - array 

def ft_red(array):
    array[..., [1, 2]] = 0
    return array

def ft_green(array):
    array[..., [0, 2]] = 0
    return array

def ft_blue(array):
    array[..., [0, 1]] = 0
    return array

def ft_grey(array):
    array = array.astype(float)
    
    array[..., 0] /= 3
    array[..., 1] /= 3
    array[..., 2] /= 3

    grey = array.astype(np.uint8).sum(axis=-1)
    return np.stack([grey, grey, grey], axis=2)

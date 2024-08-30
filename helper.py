import numpy as np


def find_weighted_average(scores_array: np.array, weights_array: np.array):
    """Compute the weighted average of student scores."""
    return np.dot(scores_array, weights_array)


def add_arrays(scores_array: np.array, weights_array: np.array):
    """Compute the element-wise sum of two arrays."""
    return np.add(scores_array, weights_array)

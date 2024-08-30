import time

import numpy as np

from helper import find_weighted_average


def process_lists(scores: list, weights: list):
    # Convert lists to numpy arrays
    scores_array = np.array(scores)
    weights_array = np.array(weights)

    # Weighted average
    result = find_weighted_average(scores_array, weights_array)
    return result


if __name__ == "__main__":
    student_scores = [85, 90, 78]
    assignment_weights = [0.4, 0.4, 0.2]

    start_time = time.time()

    result = process_lists(student_scores, assignment_weights)

    end_time = time.time()

    print("Result:", result)

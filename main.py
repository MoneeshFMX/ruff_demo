
from helper import find_weighted_average, add_arrays
import time
import numpy as np
import os



    
def process_lists( scores:list, weights : list):
    # Convert lists to numpy arrays
    scores_array=np.array(scores)
    weights_array= np.array( weights )
    
    # Weighted average
    result = find_weighted_average( scores_array , weights_array )
    
    random_var = result * 2
    
    return result





if __name__ == "__main__":
    student_scores=[85,90,78]
    assignment_weights=[ 0.4, 0.4 , 0.2]
    
    
    start_time = time.time()
    
    result =process_lists(student_scores, assignment_weights)
    
    end_time = time.time()
    
    print( f"Function took { end_time- start_time:.2f} seconds to execute")
    
    print("Result:", result)






import numpy as np
import sys

sys.set_int_max_str_digits(1000000)

def power(matrix: np.array, n : int) -> np.array:
    result = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]], dtype = object)

    while n:
        if n % 2 == 1:
            result = np.dot(matrix, result)
        
        matrix = np.dot(matrix, matrix)
        n = n//2
    
    return result

def padovan(n: int) -> int:
    if n in [0, 1, 2]:
        return 1
    
    base = np.array([[1], [1], [1]], dtype = object)
    matrix = np.array([[0, 1, 1],[1, 0, 0], [0, 1, 0]], dtype = object)

    multiplier = power(matrix, n - 2)
    # print(multiplier)

    result = np.dot(multiplier, base)
    
    return result[0][0]



assert padovan(0) == 1, "should be 1"
assert padovan(1) == 1, "should be 1"
assert padovan(2) == 1, "should be 1"
assert padovan(3) == 2, "should be 2"
assert padovan(4) == 2, "should be 2"
assert padovan(5) == 3, "should be 3"
assert padovan(6) == 4, "should be 4"
assert padovan(7) == 5, "should be 5"
assert padovan(13) == 28, "should be 28"
assert padovan(15) == 49, "should be 49"
assert padovan(40) == 55405, "should be 55405"
assert padovan(65) == 62608681, "should be 62608681"

print(padovan(1000000)) # takes ... secs

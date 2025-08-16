import numpy as np
import sys

sys.set_int_max_str_digits(1000000)

# only applicable upto 83, because np.arry cant exceed int64
# def power(matrix: np.array, n : int) -> np.array:
#     result = np.array([[1, 0], [0, 0]], dtype=np.int64)

#     while n:
#         if n % 2 == 1:
#             result = np.dot(matrix, result)
        
#         matrix = np.dot(matrix, matrix)
#         n = n//2
    
#     return result

# only applicable upto 83, because np.arry cant exceed int64
# def fibonacci(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     base = np.array([[1], [0]], dtype = np.int64)
#     matrix = np.array([[1, 1],[1, 0]], dtype=np.int64)

#     multiplier = power(matrix, n-1)
#     # print(multiplier)

#     result = np.dot(multiplier, base)
    
#     return result[0][0]

def power(matrix: np.array, n : int) -> np.array:
    result = np.array([[1, 0], [0, 0]], dtype = object)

    while n:
        if n % 2 == 1:
            result = np.dot(matrix, result)
        
        matrix = np.dot(matrix, matrix)
        n = n//2
    
    return result

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    base = np.array([[1], [0]], dtype = object)
    matrix = np.array([[1, 1],[1, 0]], dtype = object)

    multiplier = power(matrix, n-1)
    # print(multiplier)

    result = np.dot(multiplier, base)
    
    return result[0][0]



assert fibonacci(0) == 0, "should be 0"
assert fibonacci(1) == 1, "should be 1"
assert fibonacci(2) == 1, "should be 1"
assert fibonacci(3) == 2, "should be 2"
assert fibonacci(4) == 3, "should be 3"
assert fibonacci(5) == 5, "should be 5"
assert fibonacci(6) == 8, "should be 8"
assert fibonacci(7) == 13, "should be 13"
assert fibonacci(13) == 233, "should be 233"
assert fibonacci(15) == 610, "should be 610"
assert fibonacci(40) == 102334155, "should be 102334155"

print(fibonacci(500000)) # takes 2 secs

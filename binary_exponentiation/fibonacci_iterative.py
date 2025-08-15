import sys
sys.set_int_max_str_digits(1000000)

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    n_1 = 1
    n_2 = 0
    fib_n = 0

    for _ in range(2, n+1):
        fib_n = n_1 + n_2

        n_2 = n_1
        n_1 = fib_n
    
    return fib_n


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

print(fibonacci(500000)) # takes 4-5 secs
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


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

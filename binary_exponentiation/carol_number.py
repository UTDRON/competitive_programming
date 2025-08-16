#a carol number is an integer of the form 4^n - 2^(n+1) - 1


def power (a: int, b: int) -> int:
    result = 1

    while b:
        if b % 2 == 1:
            result = result * a
        
        a = a * a
        b = b // 2

    return result


def carol(n: int) -> int:
    return power(4, n) - power(2, n+1) -1


assert carol(0) == -2, "should be -2"
assert carol(1) == -1, "should be -1"
assert carol(2) == 7, "should be 7"
assert carol(3) == 47, "should be 47"
assert carol(4) == 223, "should be 223"   

print(carol(100))
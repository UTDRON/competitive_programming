def power(a, b):
    if b == 0:
        return 1
    
    if b % 2 == 0:
        temp = power(a, b//2)
        result = temp * temp
    else:
        temp = power(a, (b-1)//2)
        result = temp * temp * a

    return result
    

assert power(5,0) == 5 ** 0, f"should be {1 ** 0}"
assert power(2,6) == 2 ** 6, f"should be {2 ** 6}"
assert power(2,5) == 2 ** 5, f"should be {2 ** 5}"
assert power(2,525) == 2 ** 525, f"should be {2 ** 525}"
# assert power(2,-1) == 2 ** -1, f"should be {2 ** -1}"
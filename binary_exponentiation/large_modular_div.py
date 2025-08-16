mod = 10 ** 9 + 7

def power(a: int, b: int) -> int:
    result = 1 % b

    while b:
        if b & 1:
            result = (result * a) % mod
        
        a = (a * a) % mod
        b = b // 2
    
    return result


print(power(2, 42))
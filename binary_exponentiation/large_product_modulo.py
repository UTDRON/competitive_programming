'''
Compute Product of 2 very Large Numbers Modulo M:
'''

def calculate(a, b, M):
    sum = 0
    
    while b:
        if b & 1:
            sum = (sum + a) % M
    
        a = (a + a) % M
        b = b // 2
    return sum


a = 1000000000
b = 1000000000
M = 1000000000 + 7
print(calculate(a, b, M))
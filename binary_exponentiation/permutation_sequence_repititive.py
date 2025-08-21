'''
Let's suppose, we are given a Permutation P and a Sequence S and we need to apply P to S for a large number of times (say K), then we can easily compute the final sequence by using Binary Exponentiation.

Examples:

P = [2, 3, 4, 1], S = [2, 1, 3, 4]
After applying permutation P to Sequence S once,
S' = [1, 3, 4, 2]
Explanation: 
S'[1] = S[P[1]] = S[2] = 1
S'[2] = S[P[2]] = S[3] = 3
S'[3] = S[P[3]] = S[4] = 4
S'[4] = S[P[4]] = S[1] = 2



After applying permutation P to Sequence S twice, 
S'' = [3, 4, 2, 1]
Explanation: 
S''[1] = S'[P[1]] = S'[2] = S[P[2]] = S[3] = 3
S''[2] = S'[P[2]] = S'[3] = S[P[3]] = S[4] = 4
S''[3] = S'[P[3]] = S'[4] = S[P[4]] = S[1] = 2
S''[4] = S'[P[4]] = S'[1] = S[P[1]] = S[2] = 1
'''

#PRO TIP
'''
in the above example instead of applying permutation P to S twice, if we apply permutation P in itself (P') and then apply it on S once, we will get the same result.

P = [2, 3, 4, 1], S = [2, 1, 3, 4]
After applying permutation P to itself once,
P' = [3, 4, 1, 2]
Explanation: 
P'[1] = P[P[1]] = P[2] = 3
P'[2] = P[P[2]] = P[3] = 4
P'[3] = P[P[3]] = P[4] = 1
P'[4] = P[P[4]] = P[1] = 2



Now, applying permutation P' to S,
S''[1] = S[P'[1]] = S[3] = 3
S''[2] = S[P'[2]] = S[4] = 4
S''[3] = S[P'[3]] = S[1] = 2
S''[4] = S[P'[4]] = S[2] = 1

'''

def execute(s: list, p: list) -> list:
    temp = [0] * len(s)

    for i in range(len(s)):
        temp[i] = s[p[i]]
    
    for i in range(len(s)):
        s[i] = temp[i]
    

    return s

def apply(s: list, p: list, k: int) -> list:
    if k == 0:
        return s
    
    result = [0] * len(s)

    while k:
        if k & 1:
            result = execute(s, p)
        
        p = execute(p, p)
        k = k // 2

    return result


P = [0, 2, 3, 4, 1]
S = [0, 2, 1, 3, 4]
K = 2
print(apply(S, P, K))
    

    

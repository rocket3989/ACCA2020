from math import gcd

def nCr(n, r):
    if n - r < r:
        r = n - r
    
    if r == 0:
        return 1
    
    p, k = 1, 1
    
    while r:
        p *= n
        k *= r
        
        m = gcd(p, k)
        
        p //= m
        k //= m
        
        n -= 1
        r -= 1
    return p
    
    
while True:
    a = int(input())
    b = int(input())
    if a == b == 0: break
    
    print(nCr(1 + b - a, 4))
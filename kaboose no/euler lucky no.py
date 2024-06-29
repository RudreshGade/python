from bisect import bisect_left
import numpy as np
import math

def binsort(a, x):
    lo = 0
    hi = len(a)
    pos = bisect_left(a, x, lo, hi)
    return pos if pos!= hi and a[pos] == x else -1

# define the function 
def f(n, p):
    return (n**2 - n + p)
    
A = np.loadtxt('prime', dtype=int)

for p in range(1, int(math.sqrt(100000000000))):
    for i in range(p):
        if -1 == binsort(A, f(i, p)):
            break
    else:
        print(p)

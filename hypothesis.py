import math
from math import floor
from decimal import Decimal, getcontext
import time

start_time = time.time()

context = getcontext()
context.prec = 1000 # Set precision to 1,000 digits

alpha = Decimal(1) / Decimal(math.sqrt(14.14))

n = 60
k = 2
print(f"Alpha: {alpha}")

D = [(alpha * Decimal(i) % Decimal(1)) for i in range(1,n+1)]
D.sort()

N = []
for i in range(0,n):
    for j in range(1,n+1):
        if D[i] == (alpha * Decimal(j) % Decimal(1)):
            N.append(j)

print("The ordering is ", N)

P = Decimal(0)
for i in range(k):
    P += floor((alpha % Decimal(1)) * (n + i))
P += 2

print('The Formulated Answer is', P)

for i in range(n):
    if N[i] == k:
        print('The Position of', k, 'th term is', i + 1)

print("Process finished in %s seconds." % (time.time() - start_time))
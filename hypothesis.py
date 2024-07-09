import math
from math import floor
from decimal import Decimal, getcontext
import time
start_time = time.time()

context = getcontext()

context.prec = 10000

alpha = 1/math.sqrt(20)

n = 100
k = 5
print(alpha)
D = [((alpha*i)%1) for i in range(n)]
D.sort()
# print(D)
N = []
for i in range(n):
    for j in range(n):
        if D[i] == ((alpha*j)%1):
            N.append(j)
print("The ordering is ",N)

# for j in range(n+1):
P = 0
for i in range(k):
    P += floor((alpha%1)*(n+i)) 
P += -n+1
print('The Formulated Answer is',P)

for i in range(n):
    if N[i] == k:
        print('The Position of',k ,'th term is',i)






# C = [n*(k+1)((i/n)-math.floor((i/n))-k*math.floor(i/n)) for i in range(k*n+n+k)]

# if D == C:
#     print("correct")
# else:
#     print("incorrect")
print("Process finished in %s seconds." % (time.time() - start_time))
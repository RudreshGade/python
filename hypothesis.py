import math
from math import floor
from decimal import Decimal, getcontext
# import pickle
import time
start_time = time.time()

context = getcontext()

context.prec = 10000
k = 4
delta = 1/2*(1+k)
#delta = (math.sqrt(5)+1)
#delta = (math.pi)**(1/3)
#delta = math.e
#delta = math.sqrt(3)-math.sqrt(2)
#delta  = math.sqrt(7)+2*math.sqrt(231)
#beta = 1/(1-(1/alpha))
#rho = 1/math.sqrt(2)
#rho = 1/math.sqrt(30)
#rho = math.sqrt(1/6)
# rho = 1/(3)
rho = 0 

n = 1000

D = [(math.floor(delta*i + rho)) for i in range(1, n)]
m= max(D)

C=[]
C.extend(range(0,m))
C.extend(range(0,m))
C.extend(range(0,m))
# C.extend(range(0,m))
# C.extend(range(0,m))
# C.extend(range(0,m))
C.extend(D)
C.sort()
#print(C)

R = []
R.extend(range(0,m))
R.extend(range(0,m))
R.extend(range(0,m))
R.extend(range(0,m))
# R.extend(range(0,m))
# R.extend(range(0,m))
# R.extend(range(0,m))
# R.extend(range(0,m))
# R.extend(range(0,m))
R.extend(D)
R.sort()
#print(R)

A=[]
B=[]
for i in range(1,n+1):
    A.append(2*(i) - 1 - R[i-1])
    B.append(2*(i) + C[i-1])

print(A)
#print(B)


if A == A:
    print("correct")
else:
    print('incorrect')

print("Process finished in %s seconds." % (time.time() - start_time))
import math
from math import floor
from decimal import Decimal, getcontext
# import pickle
import time
start_time = time.time()

context = getcontext()

context.prec = 10000


k = 1
# delta = ((k-1)-(math.sqrt(1+k**2)))/k
delta = -(2)/k
# delta = (math.sqrt(5)+1)/2
# delta = (math.pi)**(1/3)
# delta = math.sqrt(2)
# delta = math.sqrt(3)-math.sqrt(2)
# delta  = math.sqrt(7)+2*math.sqrt(231)
# beta = 1/(1-(1/alpha))
# rho = 1/math.sqrt(2)
# rho = 1/math.sqrt(30)
# rho = math.sqrt(1/6)
# rho = 1/(3)
rho = 0
print(delta)
n = 10

D = [(math.floor(delta*i + rho)) for i in range(1, n+1)]
m= max(D)

C=[]
# C.extend(range(-m,0))
# C.extend(range(-m,0))
# C.extend(range(-m,0))
# C.extend(range(-m,0))
# C.extend(range(-m,0))
# C.extend(range(-m,0))
C.extend(D)
C.sort()
C.reverse()
#print(C)

R = []
R.extend(range(-m,0))
# R.extend(range(-m,0))
# R.extend(range(-m,0))
# R.extend(range(-m,0))
# R.extend(range(-m,0))
# R.extend(range(-m,0))
# R.extend(range(-m,0))
# R.extend(range(-m,0))
# R.extend(range(-m,0))
R.extend(D)
R.sort()
R.reverse()
#print(R)

A=[]
B=[]
for i in range(1,n+1):
    A.append(2*(i) - 1 - R[i-1])
    B.append(2*(i) + C[i-1])

print(A)
print(D)
# print(B)
for i in range(k+1,n):

    if A[i] != D[i+1]:
        print("not fixed seq", i, A[i],D[i])
        break
    # else:
    #     print(" a fixed seq")
    #     break

# def slope(delta, k):
#  return ((2*k-1)*(delta) +2)/(k*(delta)+1)


# def A1(delta, k, n):
#     return [math.floor((i * slope(delta, k))) for i in range(1, n + 1)]
# A1 = A1(delta, k, n)

# def frac(delta,k):
#     return [(i * slope(delta, k)) - math.floor((i * slope(delta, k))) for i in range(1, n + 1)]
# f = frac(delta,k)

# DIFF0 = []
# DIFF1 = []



# for i in range(0,n):

#     a = A1[i] - A[i]
#     if a == 0:
#         DIFF0.append(f[i]) 
#     else:
#         DIFF1.append(f[i])



# SortedDiff0 = sorted(DIFF0)
# SortedDiff1 = sorted(DIFF1)



# for x in SortedDiff0[:30]:
# #x = (Decimal(5).sqrt()+1)/2


#     for i in range(26):

#         b = x - x % 1

#         print(int(b), end = ', ') 

#         x = x - b

#         if x == 0:

#             break

#         else:

#             x = 1 / x
#     print()

# rh = (rho/((k*(delta))+1))

# def A2(delta, k ,rh):
#     return [math.floor((i * slope(delta, k)) - rh) for i in range(1, n + 1)]
# A2 = A2(delta, k, rh )

# if A2 == A:
#     print("correct")
# else:
#     print('incorrect')

print("Process finished in %s seconds." % (time.time() - start_time))
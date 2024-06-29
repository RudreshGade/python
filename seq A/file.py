import math
from math import floor
from decimal import Decimal, getcontext
import time
start_time = time.time()

context = getcontext()

context.prec = 10000

#delta = (math.sqrt(5)+1)/2
#delta = math.sqrt(3)
delta  = math.sqrt(2)
#beta = 1/(1-(1/alpha))
#rho = 1/math.sqrt(2)
#rho = 1/math.sqrt(3)
#rho = math.sqrt(1/3)
rho = 1/2
#rho = 0
k = 2 
n = 10000000

D = [math.floor(delta*n + rho) for n in range(1, n)]
m= max(D)

C=[]
C.extend(range(0,m))
#C.extend(range(0,m))
C.extend(D)
C.sort()
#print(C)

R = []
R.extend(range(0,m))
R.extend(range(0,m))
R.extend(D)
R.sort()
#print(R)

A = []
B = []

for i in range(1,n+1):
    A.append(2*(i) - 1 - R[i-1])
    B.append(2*(i) + C[i-1])




def slope(delta, k):
 return ((2*k-1)*(delta) +2)/(k*(delta)+1)


def A1(delta, n):
    return [math.floor((k * slope(delta, 2))) for k in range(1, n + 1)]
A1 = A1(delta, n)

def frac(delta,k):
    return [(k * slope(delta, 2)) - math.floor((k * slope(delta, 2))) for k in range(1, n + 1)]
f = frac(delta,k)

DIFF1 = []
DIFF0 = []


for i in range(n):

    a = A1[i] - A[i]
    if a == 0:
        DIFF0.append(f[i]) 
    else:
        DIFF1.append(f[i])




SortedDiff0 = sorted(DIFF0)
SortedDiff1 = sorted(DIFF1)

len0 = len(SortedDiff0)


for x in SortedDiff0[:30]:
#x = (Decimal(5).sqrt()+1)/2


    for i in range(26):

        b = x - x % 1

        print(int(b), end = ', ') 

        x = x - b

        if x == 0:

            break

        else:

            x = 1 / x
    print()

rh = (2*math.sqrt(2)-1)/14

def A2(delta, k ,rh):
    return [math.floor((k * slope(delta, k)) - rh) for k in range(1, n + 1)]
A2 = A2(delta, k, rho )

print(len(A2) - len(DIFF0))
print("Process finished in %s seconds ---" % (time.time() - start_time))
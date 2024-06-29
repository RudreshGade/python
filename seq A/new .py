import math
from math import floor
from decimal import Decimal, getcontext


#delta = (math.sqrt(5)+1)/2
delta = math.sqrt(3)
# beta = 1/(1-(1/alpha))
rho = 1/math.sqrt(2)
#rho = 0
k = 2 
n = 200000

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

A=[]
B=[]
for i in range(1,n):
    A.append(2*(i) - 1 - R[i-1])
    B.append(2*(i) + C[i-1])

#print(A)
#print(B)


def slope(delta, k):
 return ((2*k-1)*(delta) +2)/(k*(delta)+1)


def A1(delta, n):
    return [(k * slope(delta, 2)) for k in range(1, n + 1)]
A1 = A1(delta, n)

# def frac(delta,k):
#     return [(k * slope(delta, 2)) - math.floor((k * slope(delta, 2))) for k in range(1, n + 1)]
# f = frac(delta,k)

def DIFF0(A1, A, n):
    DIFF0 = []

    for i in range(n-1):
        a = A1[i] - A[i]
        if a < 1:
            DIFF0.append(a) 


    return DIFF0

def DIFF1(A1, A, n):
    DIFF1 = []


    for i in range(n-1):
        a = A1[i] - A[i]
        if a >= 1:
            DIFF1.append(a) 

    return DIFF1


DIFF0= DIFF0(A1, A, n)
DIFF1 = DIFF1(A1, A, n)
SortedDiff0 = sorted(DIFF0)
SortedDiff1 = sorted(DIFF1)


#print(SortedDiff0)
#print(SortedDiff1)
len0 = len(SortedDiff0)
for i in range(1,30):
 print(SortedDiff0[i])


context = getcontext()

context.prec = 10000


for x in SortedDiff0[:30]:
#x = (Decimal(5).sqrt()+1)/2
    b_values = []

    for i in range(26):

        b = x - x % 1

        b_values.append(int(b))

        x = x - b

        if x == 0:

            break

        else:

            x = 1 / x

    print(b_values)
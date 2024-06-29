
import math

def D(delta, rho, n):
   
    return [int((k * delta) + rho) for k in range(1, n + 1)]

def C(sequence):
  
    skipping_sequence = []
    for i in range(max(sequence) + 1):
        if i in sequence:
            skipping_sequence.extend([i, i])
        else:
            skipping_sequence.append(i)
    return skipping_sequence

def mex(S, Q):
 
    mex = Q
    while mex in S:
        mex += 1
    return mex

def mexcn(S, Q, n):
  
    mx = Q
    skip = n
    while skip > 0 or mx in S:
        if mx not in S:
            skip -= 1
        mx += 1
    return mx

def MES(skipping_sequence, n):
    A = []
    B = []
    MES = []
    t = 0
    for i in range(1, n + 1):
        if t == 0:
            r = 0
            t += 1
        else:
            r = max(A)
        an = mex(set(A) | set(B), r + 1)
        A.append(an)
        bn = mexcn(set(A) | set(B), r + 1, skipping_sequence[i - 1])
        B.append(bn)
        MES.append(an)
    return MES

# Example usage
#delta = (2+math.sqrt(10))/3
delta = (1+math.sqrt(5))/2
#alpha = math.sqrt(23)
#delta = math.sqrt(3)
#alpha = 2*math.sqrt(2/3)
#rho = 1/(math.sqrt(2))
rho = 0
n =10000

D = D(delta, rho, n)
print(f"The first {n} terms of the non-homogeneous defining sequence for delta = {delta} are:")
print(D)

C = C(D)
print(f"The skipping sequence with {n} terms is:")
print(C)

MES = MES(C, n)
print(f"The MES sequence with {n} terms is:")
print(MES)

B = [i for i in range(1, max(MES) +1) if i not in MES]
print(f"The complementary sequence of the MES sequence is:")
print(B)

from math import floor

def slope(delta, k):
    return ((2*k-1)*(delta) +2)/(k*(delta)+1)

def A1(delta, n):
    return [floor(k * slope(delta, 2)) for k in range(1, n + 1)]

def DIFF(A1, MES, n):
    return [A1[i] - MES[i] for i in range(n)]

def F(delta, n):
    return [(i * slope(delta, 2)) - floor((i * slope(delta, 2))) for i in range(n)]

def Diff1(DIFF, F, n):
    return [F[i] for i in range(1, n) if DIFF[i] == 0]

def Diff2(DIFF, F, n):
    return [F[i] for i in range(n) if DIFF[i] == 1]



A1_val = A1(delta, n)
print(f"The first {n} terms of the homogeneous defining sequence for delta = {delta} are:")
print(A1_val)

DIFF_val = DIFF(A1_val, MES, n)
print(f"The first {n} terms of the difference sequence for delta = {delta} are:")
print(DIFF_val)

F_val = F(delta, n)
print(f"the first {n} terms of fractional part of homogeneous is ")
print(F_val)

Diff1_val = Diff1(DIFF_val, F_val, n)
print(f"the sequence G is ")
print(Diff1_val)

Diff2_val = Diff2(DIFF_val, F_val, n)
print(Diff2_val)

SortedDiff0 = sorted(Diff1_val)
SortedDiff1 = sorted(Diff2_val)

print(SortedDiff0)
len0 = len(SortedDiff0)

from decimal import Decimal, getcontext

from math import floor




context = getcontext()

context.prec = 10000


for x in SortedDiff0[-100:]:
#=x = math.sqrt(3)
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
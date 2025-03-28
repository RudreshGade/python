import math
import numpy as np
import matplotlib.pyplot as plt

# A = np.loadtxt('prime', dtype=int)

L = []
with open('prime', 'r') as pr:
    A = np.loadtxt('prime', dtype=int)
    for j in range(1000000):
        a = 0
        # for i in range(1,j):
        if A[j+1]-A[j] == 2:
                # print(A[i])
                # a += 1
            L.append(A[j])    
            print(A[j],A[j+1])
print(len(L))
fig, ax = plt.subplots()            
ax.plot(range(len(L)), L)
plt.show() 

# a = 0
#         if A[i]%9 == 5:
#             a += 1

# b = len(A) - a

# print(a,b)

    

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from math import floor 

n = 5
d = 5
g = nx.Graph()

for k in range(d):
    for i in range(k*n+1,(k+1)*n):
        g.add_edge(i,i+1)
    g.add_edge((k+1)*n,k*n+1)

# for j in range(1,n+1,floor(n/2)):
for i in range(d):
    g.add_edge(n*i+1,(i+1)*n+1)

L = nx.laplacian_matrix(g)
e = sorted(np.linalg.eigvals(L.toarray()))
print(f"Second smallest eigenvalue : {e[1]}")

nx.draw(g)
plt.show()

# find fiedler value of subgraphs with 1 vertex removed for all vertices one at a time 
A = [e[1]]

for i in range(1, d * n + 2):
    g_i = g.copy()
    g_i.remove_node(i)
    S_i = nx.laplacian_matrix(g_i)
    E_i = sorted(np.linalg.eigvals(S_i.toarray()))
    print(f"Second smallest eigenvalue after removing node {i}: {E_i[1]}")
    # nx.draw_networkx(g_i)
    # plt.show()
    A.append(E_i[1]/e[1])


fig, ax = plt.subplots()            
ax.plot(range(1,d*n+2), A[1:])  
plt.show() 
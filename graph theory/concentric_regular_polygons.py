import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
n = 5 # Define the no. of vertices in one polygon
d = 40  # Define the no of polygons 
g = nx.Graph()

# Construct the spider web of n polygons 

for k in range(d):
    for i in range(k*n+1,(k+1)*n):
        g.add_edge(i,i+1)
    g.add_edge((k+1)*n,k*n+1)

for k in range(d-1):
    for i in range(1,n+1):
        g.add_edge(k*n+i,(k+1)*n+i)
for i in range(1,n+1):
    g.add_edge(d*n+1,i)

L = nx.laplacian_matrix(g)
e = sorted(np.linalg.eigvals(L.toarray()))
print(f"Second smallest eigenvalue : {e[1]}")
# nx.draw_spectral(g)
# plt.show()

# find fiedler value of subgraphs with 1 vertex removed for all vertices one at a time 
A = [e[1]]

for i in range(1, d * n + 2,n):
    g_i = g.copy()
    g_i.remove_node(i)
    S_i = nx.laplacian_matrix(g_i)
    E_i = sorted(np.linalg.eigvals(S_i.toarray()))
    print(f"Second smallest eigenvalue after removing node {i}: {E_i[1]}")
    # nx.draw_networkx(g_i)
    # plt.show()
    A.append(E_i[1])


fig, ax = plt.subplots()            
ax.plot(range(1,d*n+2,n), A[1:])  
plt.show() 
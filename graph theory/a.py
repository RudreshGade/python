import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from math import floor 
import networkx as nx
import scipy as scipy

n = 5
d = 4
g = nx.Graph()

# Construct the spider web of n polygons 

for k in range(d):
    for i in range(k*n+1,(k+1)*n):
        g.add_edge(i,i+1)
    g.add_edge((k+1)*n,k*n+1)

for k in range(d-1):
    for i in range(1,n+1):
        g.add_edge(k*n+i,(k+1)*n+i)
# for i in range(1,n+1):
#     g.add_edge(d*n+1,i)
g.remove_node(1)

# nx.draw(g)
# plt.show()
nodelist = list(g)
A = nx.to_scipy_sparse_array(g, nodelist=nodelist, weight="weight", format="csr")
n, m = A.shape
diags = A.sum(axis=0)  # 1 = outdegree, 0 = indegree
D = scipy.sparse.spdiags(diags.flatten(), [0], m, n, format="csr")

print((D - A).todense())
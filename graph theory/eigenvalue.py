# import numpy as np
# from numpy.linalg import eig

# a = np.array([[3,-1,-1,-1,0], 
#             [-1,4,-1,-1,-1],
#             [-1,-1,4,-1,-1],
#             [-1,-1,-1, 4,-1],
#             [0,-1,-1,-1,3]])
# w,v=eig(a)
# print('E-value:', w)
# print('E-vector', v)

import networkx
import matplotlib.pyplot as plt

n = 3
m = 1
g = networkx.complete_graph(n-1)
g.add_node(n)
g.add_edges_from([(n,i) for i in range(m)])

L = networkx.laplacian_matrix(g)
e = sorted(np.linalg.eigvals(L.toarray()))

print(e[1])
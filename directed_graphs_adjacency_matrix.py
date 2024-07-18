dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)] #sample edges of a directed graph
size = n
import numpy as np
W = np.zeros(shape=(n,n,2))
for (i,j,d) in dedges:
  # updates the values as per the edges and their weights in the graphs
  W[i,j,0] = 1 # W[i,j,0] = 1 if the (i,j) edge exists in graph
  W[i,j,1] = d
print(W)

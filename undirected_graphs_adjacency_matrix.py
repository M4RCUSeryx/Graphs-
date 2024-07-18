dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)] #sample edges of a directed graph
size = n #n be the number of vertices in graph
edges = dedges + [(j,i,d) for (i,j,d) in dedges]
import numpy as np
W = np.zeros(shape=(size,size,2))
for (i,j,d) in edges:
  W[i,j,0] = 1
  W[i,j,1] = d
print(W)

WL = {}
for i in range(size):
  WL[i] = []
for (i,j,d) in dedges:
  WL[i].append((j,d))
print(WL)


import numpy as np
import matplotlib.pyplot as plt

A=np.random.random([10,3])

# print(A)

plt.plot(A[:,0],A[:,1],'o')
for i,e in enumerate(A[:,0]):
    plt.text(A[i,0],A[i,1],"  {0} ,{1}".format(i,round(A[i,2],1)))

idx=np.array([3,4,6,2,8,1,9,5,7,0])
plt.plot(A[idx,0],A[idx,1])
plt.show()
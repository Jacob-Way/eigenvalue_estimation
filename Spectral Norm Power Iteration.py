from matplotlib import pyplot as plt
import numpy as np
import sys
#number of dimensions
n=3

m=3
#define matrix M
M=np.random.normal(0,1,[n,m])+np.random.normal(0,1,[n,m])*1j

svs = np.linalg.svd(M)[1]
norm = max(svs)
print(norm)

test = np.random.normal(0,1,m)
test = test/np.linalg.norm(test)

testvals = np.zeros(1000)

for i in range(1000):
    test = np.matmul(M,test)
    test = test/np.linalg.norm(test)
    testvals[i]=np.abs(test[0])
tnorm = np.linalg.norm(np.matmul(M,test))
print(tnorm)
print(tnorm-norm)
plt.plot(testvals)
plt.show()

from matplotlib import pyplot as plt
import numpy as np
import sys
from basics import *
#number of dimensions
n = 3
#number of sample matrices
m=5000

#M = np.random.random([n,n])+np.random.random([n,n])*1j

#M=np.matrix([[1,0,0],[0,1,0],[0,0,1]],dtype=complex)

#define basic matrix
#M=0.5*np.eye(n,dtype=complex)+0.5*np.random.normal(0,1,[n,n])+np.random.normal(0,1,[n,n])*1j
M=10*np.eye(n)+np.random.normal(0,1,[n,n])+np.random.normal(0,1,[n,n])*1j

#calculate Gershgorin circles


(a,R)=gersh(M)
(a_,R_)=gersh(M.transpose())
#sample matrices with the same diagonal elements and column sums
e = np.zeros([n,m],dtype=complex)
for i in range(m):
    A=np.zeros([n,n],dtype=complex)
    for j in range(n):
        r = np.random.random(n-1)*2+np.random.random(n-1)*2j-1-1*j
        r=r/sum(abs(r))*R[j]
        A[:,j]=np.insert(r,j,a[j])
    #print(gersh(A))
    e[:,i]=sorted(np.linalg.eig(A)[0],key=abs)


#plot everything
plt.figure(figsize=(10,10))
#plt.xlim(-5,5)
#plt.ylim(-5,5)

for i in range(n):
    plt.fill(R[i]*np.sin(np.linspace(0,2*np.pi,100))+np.real(a[i]),
            R[i]*np.cos(np.linspace(0,2*np.pi,100))+np.imag(a[i]),
            color='black',
            zorder=-1,
            alpha=0.5
            )
    plt.fill(R_[i]*np.sin(np.linspace(0,2*np.pi,100))+np.real(a_[i]),
            R_[i]*np.cos(np.linspace(0,2*np.pi,100))+np.imag(a_[i]),
            color='red',
            zorder=0,
            alpha=0.5
            )
#sample eigenvalues
plt.scatter(np.real(e[0]),
            np.imag(e[0]),
            marker="."
            )
plt.scatter(np.real(e[1]),
            np.imag(e[1]),
            marker="."
            )
plt.scatter(np.real(e[2]),
            np.imag(e[2]),
            marker="."
            )
plt.scatter(np.real(a),
            np.imag(a),
            marker="o"
            )
plt.legend()
#plt.scatter(0.5,0.5,s=(555)**2,marker="o")
plt.show()

import numpy as np
def gersh(A):
    #Input a matrix, output a tuple containing the centers of the cirles and the radii of the circles
    n=len(A)
    a = np.zeros(n,dtype=complex)
    R = np.zeros(n)
    for i in range(n):
        a[i] = A[i,i]
        for j in range(n):
            R[i] = R[i]+abs(A[i,j])
        R[i]=R[i]-abs(a[i])
    return([a,R])

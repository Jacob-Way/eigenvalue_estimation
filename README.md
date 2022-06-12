# eigenvalue_estimation
A collection of eigenvalue estimation algorithms
##1. Gershgorin Circle theorem
This theorem puts bounds on the values of eigenvalues of complex square matrices.
Given the sum of absolute values of the rows not including diagonal entries, as well as the diagonal entries, one can construct circles whose union encloses the eigenvalues of the matrix.
###Gershgorin 1
This script generates a random complex 3x3 matrix, then calculates and displays the Gershgorin circles of the matrix and its complement. The matrix's circles are in black and the complement's circles are in red. The eigenvalues must be in at least one circle of each color. The script also generates a sample of other matrices with the same Gershgorin circles and plots their eigenvalues.

import numpy as np

A = np.array([[2.4, -0.8, -0.7],
              [0.5, 1.5, 0.7],
              [-0.1, 0.8, 2.1]])

b=np.array([0.9,2.7,2.8])

(m,n)=A.shape         

R=np.triu(A)
D=np.triu(A)

j=0
l=0

for j in range (0,n):
    for l in range (0,m):
        if j==l:
            D[j,l]=A[j,l]
            
        if j!=l:
            D[j,l]=0      
i=0
k=0

for i in range (0,n):
    for k in range (0,m):
        if i==k:
            R[i,k]=0
            
        if i!=k:
            R[i,k]=A[i,k]
            
print("\nR:\n",R,"\nD:\n",D,"\nb:\n",b)

x=np.linalg.solve(D+R,b)

print("\nSoluzione:\n",x)

        
        
import numpy as np

A = np.array([[2.4, -0.8, -0.7],
              [0.5, 1.5, 0.7],
              [-0.1, 0.8, 2.1]])

ID=np.array([[1,0,0],
             [0,1,0],
             [0,0,1]])

b=np.array([0.9,2.7,2.8])

k=0
(m,n)=A.shape

D=np.array([])

def elleu(A):
    (m,n)=A.shape
    L=np.eye(n)
    for k in range(0,n-1):
        if A[k,k]==0:
            print("pivot nullo")
            return [],[]
        for i in range(k+1,n):
            L[i,k]=A[i,k]/A[k,k]
            for j in range(k+1,n):
                A[i,j]=A[i,j]-L[i,k]*A[k,j]
    U=np.triu(A)
    print("l:\n",L,"\n\nU:\n",U)
            

D=np.triu(A)

j=0
l=0

for j in range (0,n):
    for l in range (0,m):
        if j==l:
            D[j,l]=A[j,l]
            
        if j!=l:
            D[j,l]=0
            
print("R:\n",R,"\nD:\n",D)

    
    
    
    

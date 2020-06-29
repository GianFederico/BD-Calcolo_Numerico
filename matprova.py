import numpy as np

A=np.array([[2.4,-0.8,-0.7],[0.5,1.5,0.7],[-0.1,0.8,2.1]])

(m,n)=A.shape

b=np.array([0.9,2.7,2.8])

def Gauss(A,b,toll,toll_fin,maxiter):

    i=0
    j=0
    k=0
    l=0

    U=np.triu(A)
    for i in range (0,n):
        for j in range (0,m):
            
            if i==j:
                U[i,j]=0
                
    print("u:\n",U)
    
    L=np.tril(A)
    for k in range (0,m):
        for l in range (0,n):
            
            L[k,l]=b[k]-U[k,l]
            
    print(L)
                
    
    
    
    
    
    
Gauss(A,b,1e-2,1e-6,32)
                
    

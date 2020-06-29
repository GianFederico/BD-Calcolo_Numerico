import numpy as np
import scipy as sp

def f(x):
    return np.cos(x)-x**3
def df(x):
    return -3*x**2-np.sin(x)

A=np.zeros((3,3))
A[0,0]=2.4; A[0,1]=-0.8; A[0,2]=-0.7;
A[1,0]=0.5; A[1,1]=1.5; A[1,2]=0.7;
A[2,0]=-0.1; A[2,1]=0.8; A[2,2]=2.1;

b=np.zeros((1,3))
b[0,0]=0.9; b[0,1]=2.7; b[0,2]=2.8; 



def traub(f,df,x0,toll,maxiter):
    numiter=0
    d=df(x0)
    
    
    y=x0-(f(x0)/d)
    x1=y-(f(y)/d)
    
    rerr=abs(x1-x0)/abs(x1)
    
    while numiter<maxiter and rerr>toll:
       x0=x1
       d=df(x0)
       y=x0-(f(x0)/df(x0))
       x1=y-(f(y)/df(y))
       
       rerr=abs(x1-x0)/abs(x1)
       numiter=numiter+1
       
    print(x1,numiter)
     
traub(f,df,1,1e-6,22)

#_______________________________________________

def gauss(A,b,toll,x0,maxiter):###############################################err################################################
    U=np.zeros
    U=A.copy()
    
    for i in range (1,A.shape[0]+1):
        for j in range (1,i+1):
            U[i-1,j-1]=0
            
    L=np.zeros
    L=A.copy()
    for i in range (A.shape[0]-1,0,-1):
        for j in range (A.shape[1],i,-1):
            L[i-1,j-1]=0
            
    rerr=toll+1
    numiter=0
    x1=x0

    while rerr>toll/np.linalg.norm(x1,1) and numiter<maxiter:

        x1=b-np.dot(U,x0)
        x1=sp.linalg.solve_triangular(L,x1)
        rerr=np.linalg.norm((x1-x0),1)/(np.linalg.norm(x1,1))
        x0=x1.copy()
        
        numiter=numiter+1
        
    print(x1,numiter)
    
gauss(A,b,1e-6,[1,1,1],22)
    





        

import numpy as np

def f(x):
    return np.sin(x)-x**3

A=np.zeros((3,3))
A[0,0]=2.4; A[0,1]=-0.8; A[0,2]=-0.7;
A[1,0]=0.5; A[1,1]=1.5; A[1,2]=0.7;
A[2,0]=-0.1; A[2,1]=0.8; A[2,2]=2.1;

b=np.zeros((1,3))
b[0,0]=0.9; b[0,1]=2.7; b[0,2]=2.8; 

def steffensen (f,x0,toll,maxiter):
    numiter=0
    rerr=toll+1
    
    while rerr>toll and numiter<maxiter:
        x1=x0-((f(x0)**2)/(f(x0+f(x0))-f(x0)))
        rerr=abs(x1-x0)/abs(x1)
        
        x0=x1
        
        numiter=numiter+1
        
    residuo=f(x1)
        
    print(x1,numiter,residuo)
    
steffensen(f,1,1e-12,44)

#____________________________________________________

def jacobi(A,b,x0,toll,maxiter):
    numiter=0
    rerr=toll+1
    
    R=A.copy()
    for i in range (0,R.shape[0]):
        R[i,i]=0
    
    D=A-R
    
    x1=x0
      
    while rerr>toll/np.linalg.norm(x1,np.inf) and numiter<maxiter:
        x1=np.linalg.solve(D,(b-(np.dot(R,x0))))
        rerr=np.linalg.norm((x1-x0),np.inf)/np.linalg.norm(x1,np.inf)
        x0=x1
        
    residuo=np.linalg.norm((np.dot(A,x1)-b),np.inf)
    
    print(x1,numiter,residuo)
    
jacobi(A,b,[0.9,0.9,0.9],1e-5,33)#############################err input###############################################
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
        

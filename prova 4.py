import numpy as np

def f(x):
    return np.cos(x)-x**3

A=np.zeros((3,3))
A[0,0]=-0.5; A[0,1]=-0.1; A[0,2]=0.8;
A[1,0]=-0.7; A[1,1]=0.1; A[1,2]=0;
A[2,0]=-0.5; A[2,1]=-0.1; A[2,2]=0.9;

def zeri(f,x0,h,toll,maxiter):
    numiter=0
    rerr=toll+1
    x1=0
    
    while rerr>toll and numiter<maxiter:
        numiter=numiter+1
        x1=x0-2*h*(f(x0)/(f(x0+h)-f(x0-h)))
        rerr=abs(x1-x0)/abs(x1)
        
        x0=x1
        
        
    print(x1,numiter)

zeri(f,0,5,1e-6,400)

#_________________________________________________

def potenze(A,x0,toll,maxiter):
    numiter=0
    y0=x0/np.linalg.norm(x0, 2)
    x1=np.dot(A,y0)
    v0=np.dot(y0.transpose(),x1)
    
    rerr=toll+1
    
    while rerr>toll and numiter<maxiter:
        x0=x1
        y0=x0/np.linalg.norm(x0, 2)
        x1=np.dot(A,y0)
        v1=np.dot(y0.transpose(),x1)
        
        rerr=abs(v1-v0)
        
        v0=v1
        numiter=numiter+1
        
    print(v1,numiter)
    
potenze(A,[1,1,1],1e-5,22)
        
        
    
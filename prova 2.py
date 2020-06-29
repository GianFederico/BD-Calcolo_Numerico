import numpy as np

def f(x):
    return np.sin(x)/x-x

def g(x):
    return np.sqrt(1-x**2)

def secanti(f,x0,x1,toll,maxiter):
    numiter=0
    rerr=abs(x1-x0)/abs(x1)
    
    while rerr>toll and numiter<maxiter:
        
        funz=x1-(f(x1)*(x1-x0))/(f(x1)-f(x0))
        x0=x1
        x1=funz
        rerr=abs(x1-x0)/abs(x1)
        
        numiter=numiter+1
        
    print(x1,numiter)
    
secanti(f,1,0.9,1e-9,22)

#__________________________________________________

def trapezi(g,a,b,n):
    h=(b-a)/n
    summ=(h/2)*(g(a)+g(b))
    
    for j in range (1,n-1):
        summ+=h*g(a+j*h)
        
    print(summ)
    
trapezi(g,0,1,64)

import numpy as np

def cubo (s,toll,maxiter):
    numiter=0
    x0=s
    x1=(1/3)*(2*x0+(s/x0**2))
    rerr=abs(x1-x0)/abs(x1)
    
    while rerr>toll and numiter<maxiter:
        x0=x1
        x1=(1/3)*(2*x0+(s/x0**2))        
        
        rerr=abs(x1-x0)/abs(x1)
        numiter+=1
        
    print(x1,numiter)

    
cubo(1234,1e-6,22)

#_____________________________________________________

def simpson(f,a,b,n):
    h=(b-a)/n
    In=f(a)*h/3+f(b)*h/3
    
    j=1
    i=1
    
    while j<=(n/2)-1:
        In+=(h/3)*(2*f(a+2*j*h))
        j=j+1
        
    while i<=n/2:
        In+=(h/3)*(4*f(a+(2*i-1)*h))
        i=i+1
        
    print(In)
    
simpson(np.sin,0,np.pi,16)
    
    

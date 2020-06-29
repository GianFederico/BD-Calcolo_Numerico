import numpy as np

def f(x):
    return np.sqrt(abs(1-x**2))

x0=float(input(print("primo punto: ")))
x1=float(input(print("secondo punnto: ")))
toll=float(input(print("precisione iniziale: ")))
toll_fin=float(input(print("tolleranza: ")))
maxiter=int(input(print("num max iterate: ")))
n=int(input(print("numero intervalli: ")))


def trapezi(x0,x1,toll,toll_fin,f,maxiter,n):  
    
    numiter=0
    h=(x1-x0)/n
    
        
    while toll>toll_fin and numiter<maxiter:            
        
        x1=(h/2)*(f(x0)+2*(sum(f(x0+j*h) for j in range (1,n-1)+f(n))))
    
        x0=x1
        print("soluzione apporx:",x0)
    
        toll=abs((x1-x0)/x1)
        numiter=numiter+1
        
    print("soluz:",x0,"\nnumero iterate: ",numiter)
    
    
trapezi(x0,x1,toll,toll_fin,f,maxiter,n)

    
    

    
    
        


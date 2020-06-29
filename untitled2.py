import numpy as np

def f(x):
    return np.sin(x)-x**3

x0iniziale=float(input(print("\npunto iniziale: ")))
toll=float(input(print("\nprecisione iniziale: ")))
toll_fin=float(input(print("\ntolleranza: ")))
maxiter=int(input(print("\nnumero massimo di iterate: ")))


def steffensen(f,x0iniziale,toll,toll_fin,maxiter):
    
    numiter=0
    x0=x0iniziale
    
    while toll>toll_fin and numiter<maxiter:
        
        x1= x0-((f(x0))**2/(f(x0+f(x0))-f(x0)))        
        toll=abs((x1-x0)/x1)
        x0=x1
        
        print("soluzione approx: ",x0)
        
        numiter=numiter+1
        
    print("\nSOLUZIONE:",x0,"\nNUMERO ITER: ",numiter)

steffensen(f,x0iniziale,toll,toll_fin,maxiter)



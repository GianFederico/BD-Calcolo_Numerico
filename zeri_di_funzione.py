import numpy as np

import math 

def funz(x):
    return math.cos(x)-x

nmax=22

def BISEZIONI(funz,a,b,toll,nmax):
    x=.5*(b-a)
    funzx=funz(x)
    funza=funz(a)
    niter=0
    
    print('{:2}\t {:1.15}\t {:+1.1e}'.format(niter,x,funzx))
    while .5*(b-a)>toll and niter<nmax:
        if funza*funzx<0:
            b=x
        else:
            a=x
            funza=funzx
        x=.5(a+b)
        funzx=funz(x)
        niter+=1
        print('{:2}\t {:1.15}\t {:+1.1e}'.format(niter,x,funzx))
        
    if .5*(b-a)>toll:
        niter=-1
    return (x,niter)

primo_estremo=float(input(print("primo estremo: ")))
secondo_estremo=float(input(print("secondo estremo: ")))
tolleranza=float(input(print("tolleranza: ")))

BISEZIONI(funz,primo_estremo,secondo_estremo,tolleranza,nmax)
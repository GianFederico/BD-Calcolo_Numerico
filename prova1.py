import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - np.cos(x)

def Df(x):
    return 3*x**2 + np.sin(x)


x0=1
errore = 10

while errore > 1e-10:
    
    x1 = x0 - f(x0)/ Df(x0)
    
    errore=abs(x1-x0)
    
    x0 = x1
    
print(x0)
    











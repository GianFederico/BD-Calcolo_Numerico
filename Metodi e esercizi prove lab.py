import numpy as np        

def f(x):
        return 4678

def g(x):
        return np.sin(x)/x -x
    
def h(x):
    return np.cos(x)-x**3

def h1(x):
    return -3*x**2-np.sin(x)

def j(x):
    return np.sin(x)

def l(x):
    return np.sqrt

itermax=int(input(print("iterate max: ")))
toll=float(input(print("precisione iniziale: ")))
toll_fin=float(input(print("precisione finale: ")))
x0iniziale=float(input(print("x0 iniziale:  ")))
x1iniziale=float(input(print("x1 iniziale: ")))
sottointervalli=int(input(print("sottointervalli: ")))

#_____________________________________________________________________________________________
def radice_cubica(f,itermax,toll,toll_fin):
    
    x0=1
    numiter=0
    
    
    while toll>toll_fin and numiter<itermax:
          
        x1= (1/3)*(2*x0+((f(x0))/x0**2))            #S è f(x0), xk è x0
        toll=abs((x1-x0)/x1)
        x0=x1
        
        numiter=numiter+1
        print(x0)
            
            
    print("\nradice cubica approx:",x0,"\nnumero iterate:",numiter)
    return 0

#radice_cubica(f,itermax,toll,toll_fin)
#_______________________________________________________________________________________________

def metodo_secanti(g,x0iniziale,x1iniziale,toll,toll_fin):
    
    numiter=0
    x0=x0iniziale
    x1=x1iniziale
    
    while toll>toll_fin and numiter<itermax:
        
        x2= x1-(g(x1)*(x1-x0)/(g(x1)-g(x0)))
        toll=abs((x2-x1)/x2)
        
        x0=x1
        x1=x2
        
        numiter=numiter+1
        print("radice approx:",x0)
        print("radice approx:",x1)
        
    print("\n radice: ",x1,"\n numero iterate:",numiter)
    return 0

#metodo_secanti(g,x0iniziale,x1iniziale,toll,toll_fin)
#________________________________________________________________________________
def metodo_traub(h,h1,x0iniziale,toll,toll_fin):
    numiter=0
    x0=x0iniziale
    
    while toll>toll_fin and numiter<itermax:
        y= x0-(h(x0)/h1(x0))
        x1= y-(h(y)/h1(y))
        toll=abs((x1-x0)/x1)
        
        x0=x1
        
        numiter=numiter+1
        print("radice approx:",x0)
        
    print("\n radice: ",x0,"\n numero iterate:",numiter)
    
 #metodo_traub(h,h1,x0iniziale,toll,toll_fin)
#_______________________________________________________________________________    
def simps(j,x0iniziale,x1iniziale,sottointervalli):
    
    a=x0iniziale
    b=x1iniziale
    N=sottointervalli
    
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = j(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    print("soluz:",S)
    
#simps(j,x0iniziale,x1iniziale,sottointervalli)
#_____________________________________________________________________   

def trapezi(l,x0iniziale,x1iniziale,sottointervalli):
    a=x0iniziale
    b=x1iniziale
    n=sottointervalli
    h=(b-a)/n
    
    x0=l(a)
    
    while k<n-1:
        somma=l(a)+l(x)
        
        l(a)=l(a)+l(a)
        
        k=k+1   
    
   
    
    integrale=h/2(2*np.sum(l(xj)+l(xn))[1,n-1])
    print("int:",integrale)
    
#____________________________________________________________________
   
 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

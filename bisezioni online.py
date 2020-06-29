def abs(x):
    if x < 0: return -x
    else: return x
 
def cube(x):
    return x**3
 
a = -15.0
b = 29.0
f = cube
scarto = 0.1
 
print("\n\nIntervallo iniziale: [" + str(a) + ", " + str(b) + "]")
c = (a+b)/2.0
print("Punto medio: " + str(c))
while abs(f(c)) > scarto:
    print("f(" + str(c) + ") = " + str(f(c)))

    if f(c) < 0:
        a = c
    else:
        b = c

    print("Nuovo intervallo: [" + str(a) + ", " + str(b) + "]")

    c = (a+b)/2

    print("Punto medio: " + str(c) + "\n\n")
print("Soluzione: x = " + str(c) + "\n")
print("f(" + str(c) + ") = " + str(f(c)))


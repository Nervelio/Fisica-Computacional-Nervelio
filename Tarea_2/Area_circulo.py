import numpy as np
import math

def Area(R):
    N=0
    n=0
    error=1
    while error>0.0001 and N<100000000:
        x=np.random.uniform(0,R,1000)
        y=np.random.uniform(0,R,1000)
        cont=np.sum(x*x+y*y<=R*R)
        n+=cont
        N+=1000
        error=abs(4*n/N-math.pi)/math.pi
    return 4*(n/N)*R*R
print("Digite el radio del circulo: ")
R=float(input())
print("El area es: ", Area(R))
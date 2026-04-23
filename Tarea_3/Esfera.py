# Calcular area y volumen de una esfera

import numpy as np
import math

def Volumen(R):
    N=0
    n=0
    error=1
    while error>0.0001 and N<100000000:
        x=np.random.uniform(0,R,1000)
        y=np.random.uniform(0,R,1000)
        z=np.random.uniform(0,R,1000)
        cont=np.sum(x*x+y*y+z*z<=R*R)
        n+=cont
        N+=1000
        error=abs(4*n/N-math.pi)/math.pi
    return 8*(n/N)*R*R*R

def Area(R):
    dx=0.001
    N=1000000
    x=np.random.uniform(-(R+dx),R+dx,N)
    y=np.random.uniform(-(R+dx),R+dx,N)
    z=np.random.uniform(-(R+dx),R+dx,N)
    cont_casc=np.sum((x*x+y*y+z*z>=R*R) & (x*x+y*y+z*z<=(R+dx)**2) )
    Volumen_casc=(cont_casc/N)*(2*(R+dx))**3
    return Volumen_casc/dx
    

select=0

while select!=1 and select!=2:
    print("Digite 1 para calcular el volumen de la esfera \nDigite 2 para calcular el área de una esfera")
    select= int(input())


    if select == 1:
        print("Digite el radio del circulo: ")
        R=float(input())
        print(Volumen(R))   

       
    elif select ==2:
        print("Digite el radio del circulo: ")
        R=float(input())
        print("El area es:", Area(R))
    else:
        print("Opción incorrecta.")


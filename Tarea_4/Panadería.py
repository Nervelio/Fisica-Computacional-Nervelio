"""
La panadería ``Don Juan'' prepara diariamente pan de queso. El pan se vende a \$35 por pieza y cuesta \$25 
prepararlo. Al final del día, si quedan algunas piezas por vender, otra panadería les comprará el 70\% de su 
producción a \$18 la pieza. Se sabe que la demanda diaria (en docena de piezas), cae en un rango de 3 a 7 docenas 
apegada a una distribución uniforme. La panadería ``Don Juan'' está considerando producir 
diariamente 2,3,4,5,6,7,8,9 docenas. Simula 30 días de producción y compara la ganancia diaria promedio 
según la cantidad de docenas producidas, calcula también la desviación estándar bajo estas políticas de 
orden, se considera inicialmente preparar 60 piezas.
"""
import numpy as np

costo=25
precio=35
remate=18

def Ganancia_Diaria_Prom(producción):
    ganancia_total=0
    for i in range(0,30):
        demanda = 12*np.random.uniform(3,7)
        if producción >= demanda:
            ganancia = demanda*precio + (7/10)*(producción-demanda)*remate - producción*costo
        elif demanda>producción:
            ganancia=producción*(precio-costo)
        ganancia_total+=ganancia
        i+=1
    return ganancia_total/30

suma=0
for docena in (2,3,4,5,6,7,8,9):
    producción=12*docena
    suma+=Ganancia_Diaria_Prom(producción)
    print(f"Produciendo {docena} docenas, la ganancia diaria es ${Ganancia_Diaria_Prom(producción)}")
    
promedio=suma/8
producción=0
suma_cuadrados=0
for docena in (2,3,4,5,6,7,8,9):
    producción=12*docena
    suma_cuadrados+=(Ganancia_Diaria_Prom(producción)-promedio)**2
print("La desviación estandar es:", (suma_cuadrados/8)**0.5)


    

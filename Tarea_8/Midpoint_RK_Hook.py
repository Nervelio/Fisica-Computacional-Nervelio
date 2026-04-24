import numpy as np
import matplotlib.pyplot as plt


def rk_midpoint_solver(G, t0, f0, dt, Ns):   #f0 = [posicion, velocidad]
    fn = np.array(f0, dtype=float)
    tn = t0
    
    datos = np.zeros((Ns, 3))
    datos[0] = [t0, fn[0], fn[1]] #[tiempo, posicion, velocidad]
    
    for i in range(1, Ns):
        k1 = dt * G(tn, fn)
        k2 = dt * G(tn + dt/2, fn + k1/2)
        
        fn = fn + k2
        tn = tn + dt
        
        datos[i] = [tn, fn[0], fn[1]]
        
    return datos

def sistema_resorte(t, estado):
    x, v = estado
    dxdt = v      
    dvdt = -1.0 * x 
    return np.array([dxdt, dvdt])

dt = 0.1
pasos = 200
# t=0, x=1.0, v=0.0
resultados = rk_midpoint_solver(sistema_resorte, 0.0, [1.0, 0.0], dt, pasos)

#GRÁFICA 
tiempo = resultados[:, 0]
posicion = resultados[:, 1]
velocidad = resultados[:, 2]

plt.figure(figsize=(10, 5))
plt.plot(tiempo, posicion, label='Posición (RK2)', color='darkred')
plt.plot(tiempo, velocidad, '--', label='Velocidad (RK2)', color='gray', alpha=0.7)

plt.title('Oscilador Armónico - Método del Punto Medio (RK2)', fontsize=14)
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
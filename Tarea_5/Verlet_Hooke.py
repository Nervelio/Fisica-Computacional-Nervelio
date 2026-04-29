import numpy as np
import matplotlib.pyplot as plt

def verlet_solver(a_func, x0, v0, dt, Ns):
    xout = np.zeros((Ns, 2))
    xcur = x0
    t = 0.0
    xprev = x0 - dt * v0 + 0.5 * a_func(x0, 0.0) * dt**2
    xout[0] = [t, x0]
    
    for i in range(1, Ns):
        xnext = 2.0 * xcur - xprev + dt**2 * a_func(xcur, t)
        t += dt
        xout[i] = [t, xnext]
        xprev = xcur
        xcur = xnext
        
    return xout


def aceleracion_hooke(x, t):
    k = 1.0
    m = 1.0
    return -(k/m) * x




datos = verlet_solver(aceleracion_hooke, x0=1.0, v0=0.0, dt=0.05, Ns=300)
print (datos)

tiempo = datos[:, 0]
posicion = datos[:, 1]

plt.figure(figsize=(10, 6))
plt.style.use('seaborn-v0_8-whitegrid') 

plt.plot(tiempo, posicion, 'o-', color='#1f77b4', 
         label='Trayectoria (Verlet)', linewidth=1.5, markersize=3)


plt.title('Oscilador Armónico Simple - Trayectoria', fontsize=16, fontweight='bold')
plt.xlabel('Tiempo (s)', fontsize=14)
plt.ylabel('Posición (x)', fontsize=14)


plt.grid(True, linestyle='--', alpha=0.7) 
plt.legend(loc='upper right', fontsize=12) 


plt.ylim(-1.2, 1.2) 


plt.tight_layout() 
plt.show()
import numpy as np
import matplotlib.pyplot as plt

def verlet_solver(a_func, r0, v0, dt, Ns):

    rcur = np.array(r0)
    vcur = np.array(v0)
    datos = np.zeros((Ns, 3))
    
    t=0.0
    rprev = rcur - dt * vcur + 0.5 * a_func(rcur, 0.0) * dt**2
    datos[0] = [t, rcur[0], rcur[1]]
    
    for i in range(1, Ns):
        rnext = 2.0 * rcur - rprev + dt**2 * a_func(rcur, t)
        t += dt
        datos[i] = [t, rnext[0], rnext[1]]
        rprev = rcur
        rcur = rnext
        
    return datos

R=1.0
omega = 1.0
def aceleracion_MCU(R, t):
    
    return -omega**2 * R




datos = verlet_solver(aceleracion_MCU, r0=[1.0, 0.0], v0=[0.0, omega**2/R], dt=0.05, Ns=300)
print (datos)

X = datos[:, 1]
Y = datos[:, 2]


plt.figure(figsize=(10, 6))
plt.style.use('seaborn-v0_8-whitegrid') 

plt.plot(X, Y, 'o-', color='#1f77b4', 
         label='Trayectoria (Verlet)', linewidth=1.5, markersize=3)


plt.title('MCU - Trayectoria', fontsize=16, fontweight='bold')
plt.xlabel('X', fontsize=14)
plt.ylabel('Y', fontsize=14)


plt.grid(True, linestyle='--', alpha=0.7) 
plt.legend(loc='upper right', fontsize=12) 


plt.ylim(-1.2, 1.2) 

plt.axis('equal')
plt.tight_layout() 
plt.show()
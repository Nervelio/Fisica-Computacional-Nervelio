import numpy as np
import matplotlib.pyplot as plt

def rk2_quantum_solver(G, x0, psi0, dx, Ns, E):

    fn = np.array(psi0, dtype=float)
    xn = x0
    retvals = np.zeros((Ns, 2))
    retvals[0] = [xn, fn[0]]
    
    for i in range(1, Ns):
        
        k1 = dx * G(xn, fn, E)
        k2 = dx * G(xn + dx/2, fn + k1/2, E)
        
        fn = fn + k2
        xn = xn + dx
        retvals[i] = [xn, fn[0]]
    return retvals


def schrodinger_system(x, estado, E):
    psi, phi = estado # phi es dpsi/dx
   
    if abs(x) < 2:
        V = 0
    else:
        V = 50 
    
    dpsi_dx = phi
    dphi_dx = 2 * (V - E) * psi
    return np.array([dpsi_dx, dphi_dx])


dx = 0.01
Ns = 500
x_inicio = -2.5

psi_init = [0.001, 0.0] 


sol_E1 = rk2_quantum_solver(schrodinger_system, x_inicio, psi_init, dx, Ns, E=1.118)
sol_E2 = rk2_quantum_solver(schrodinger_system, x_inicio, psi_init, dx, Ns, E=1.119) #4.8


plt.figure(figsize=(10, 6))
plt.plot(sol_E1[:, 0], sol_E1[:, 1], label='E = 1.118   (Estado base aproximado)')
plt.plot(sol_E2[:, 0], sol_E2[:, 1], label='E = 1.119 (Primer estado excitado)')
plt.axvspan(-2, 2, color='gray', alpha=0.2, label='Pozo de Potencial')
plt.title('Función de Onda $\psi(x)$ calculada con RK2')
plt.legend()
plt.grid(True)
plt.show()
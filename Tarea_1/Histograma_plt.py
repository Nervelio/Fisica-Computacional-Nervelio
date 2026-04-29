import numpy as np
import matplotlib.pyplot as plt

x=np.random.normal(0,1,1000)

plt.hist(x,bins=50,density=True)
plt.xlabel("x")
plt.ylabel("probabilidad")
plt.title("Histograma de distribución uniforme")


plt.show()
print(type(x))
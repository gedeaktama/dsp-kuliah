import numpy as np
import matplotlib.pyplot as plt

# Indeks waktu diskrit
n = np.arange(0, 40)

# Contoh sinyal diskrit: kombinasi sinus dan kosinus
x = 2*np.sin(0.2*np.pi*n) + 0.5*np.cos(0.05*np.pi*n)

# Plot sinyal
plt.stem(n, x, basefmt=" ")
plt.title("Contoh Sinyal Diskrit")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 15)
x = np.where(n >= 0, 1, 0)

plt.stem(n, x, basefmt=" ")
plt.title("Sinyal Step Diskrit")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()
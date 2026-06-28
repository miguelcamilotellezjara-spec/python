import numpy as np

# Datos del sistema para k = 82
H = np.array([[1.2, 0.4], [0.4, 1.0]])
x = np.array([2, 2])
n = np.array([0.02, -0.04])

# Cálculo de la señal recibida y recuperación
y = np.dot(H, x) + n
x_est = np.dot(np.linalg.inv(H), y)

print(f"Determinante: {np.linalg.det(H)}")
print(f"Señal recibida y: {y}")
print(f"Señal recuperada x_est: {x_est}")

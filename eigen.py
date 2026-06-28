import numpy as np
A = np.array([[3, -2], [-6, 2]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Valores propios (Eigenvalues):", eigenvalues)
print("Vectores propios (Eigenvectors):", eigenvectors)

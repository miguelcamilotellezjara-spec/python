import sympy as sp

# Definimos las variables simbólicas
x, y, z = sp.symbols('x y z')

# 1. Construir la matriz asociada A
# Definimos la transformación basada en T(x, y, z) = (x + y, 2*x + 2*y, z)
T = sp.Matrix([x + y, 2*x + 2*y, z])

# Extraemos la matriz asociada respecto a las variables [x, y, z]
A = T.jacobian([x, y, z])
print("1. Matriz asociada A:")
sp.pprint(A)
print("-" * 40)

# Paso intermedio: Reducción por filas (Forma Escalonada Reducida)
# rref() devuelve la matriz reducida y una tupla con los índices de las columnas con pivote
A_rref, pivotes = A.rref()
print("Forma escalonada reducida de A:")
sp.pprint(A_rref)
print(f"Columnas con pivote: {pivotes}")
print("-" * 40)

# 2. Determine N(T) e Im(T)
# El núcleo (nullspace) se calcula directamente desde la matriz
nucleo = A.nullspace()
# La imagen (columnspace) se genera con las columnas que tienen pivotes
imagen = A.columnspace()

print("2. Núcleo N(T) (Base):")
sp.pprint(nucleo)
print("\nImagen Im(T) (Base):")
sp.pprint(imagen)
print("-" * 40)

# 3. Calcule nulidad(T) y rango(T)
nulidad = len(nucleo)
rango = A.rank()  # O también len(imagen)

print(f"3. Nulidad(T) = {nulidad}")
print(f"   Rango(T) = {rango}")
print("-" * 40)

# 4. Verifique el teorema rango-nulidad
# Dimensión del espacio de dominio (R^3)
dim_dominio = A.shape[1] 

print("4. Verificación del Teorema Rango-Nulidad:")
print(f"   Rango ({rango}) + Nulidad ({nulidad}) = {rango + nulidad}")
print(f"   Dimensión del dominio = {dim_dominio}")
print(f"   ¿Se cumple el teorema?: {rango + nulidad == dim_dominio}")

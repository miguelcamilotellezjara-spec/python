# ==============================================================================
# FRAMEWORK: VERIFIABLE GEOMETRIC AND MATERIAL COMPUTING (PROTOTIPO ALQUÍMICO)
# Proyecto: Anisotropic Topology and Aesthetic Constraints in Generative Subtractive Form
# Autor: Miguel Camilo Téllez Jara
# Carrera: Ingeniería en Redes y Análisis de Datos
# Institución: Universidad Técnica Particular de Loja (UTPL)
# Fecha: 28/06/2026
# Descripición: Simulación numérica de propagación de tensores de tensión (stress)
#                y fractura anisotrópica inducida en sustratos heterogéneos.
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt

def simular_impacto_anisotropico(dimensiones=(50, 50), punto_impacto=(0, 25), fuerza=100, angulo_grano_rad=np.pi/4):
    """
    Simula el campo escalar de tensiones internas inducido por un impacto puntual 
    sobre un dominio discreto bidimensional con anisotropía lineal orientada.
    
    Parámetros:
    -----------
    dimensiones : tuple (X, Y)
        Resolución de la malla discreta que representa el bloque de material.
    punto_impacto : tuple (x, y)
        Coordenadas de la singularidad (aplicación de la fuerza exterior).
    fuerza : float
        Magnitud escalar de la energía entrante.
    angulo_grano_rad : float
        Orientación angular del vector director que define la veta/grano (campo anisotrópico).
        
    Retorna:
    --------
    campo_tension : ndarray
        Matriz bidimensional con los gradientes de atenuación y concentración de stress.
    """
    X, Y = dimensiones
    # Inicialización del tensor de tensiones escalar sobre el dominio espacial
    campo_tension = np.zeros(dimensiones)
    
    # Vector unitario director (\hat{v}_g) que parametriza la orientación del grano
    vector_grano = np.array([np.cos(angulo_grano_rad), np.sin(angulo_grano_rad)])
    
    for x in range(X):
        for y in range(Y):
            # 1. COMPONENTE ISOTRÓPICA: Evaluación del vector de distancia euclidiana (\vec{r})
            # En un medio puramente isotrópico (cohesión atómica homogénea), la propagación
            # de la onda de choque radial disiparía la energía equitativamente en 360 grados.
            vector_distancia = np.array([x - punto_impacto[0], y - punto_impacto[1]], dtype=float)
            distancia = np.linalg.norm(vector_distancia)
            
            if distancia == 0:
                campo_tension[x, y] = fuerza
                continue
                
            # Normalización del vector dirección del impacto (\hat{r})
            direccion_impacto = vector_distancia / distancia
            
            # 2. COMPONENTE ANISOTRÓPICA: Proyección ortogonal y producto escalar |\hat{r} \cdot \hat{v}_g|
            # Representa matemática y algorítmicamente las discontinuidades físicas del material.
            # La alineación de la onda de choque con los planos de clivaje/fibras minimiza la 
            # resistencia al desplazamiento, concentrando los vectores de tensión y facilitando la fractura.
            alineacion_grano = np.abs(np.dot(direccion_impacto, vector_grano))
            
            # 3. MODELO DE DISIPACIÓN Y AMPLIFICACIÓN DINÁMICA
            # Atenuación geométrica por ley de potencias inversa (simulación aproximada de disipación elástica)
            atenuacion = 1.0 / (distancia ** 1.5)
            # Factor anisotrópico: Modula y distorsiona el frente de onda esférico original
            factor_anisotropico = 1.0 + 2.0 * alineacion_grano
            
            # Asignación del estado de tensión localizado en la celda (x, y)
            campo_tension[x, y] = fuerza * atenuacion * factor_anisotropico

    return campo_tension


# --- EJECUCIÓN DEL EXPERIMENTO GEOMÉTRICO (VALIDACIÓN VISUAL) ---
if __name__ == "__main__":
    print("[INFO] Iniciando el proceso de individuación de la materia...")
    
    # Configuración del entorno físico de prueba (Boundary Conditions)
    # Bloque de 60x60 celdas, impacto en la frontera elástica superior centro, grano con inclinación de 30°
    angulo_vetas = np.radians(30) 
    matriz_tension = simular_impacto_anisotropico(
        dimensiones=(60, 60), 
        punto_impacto=(0, 30), 
        fuerza=150, 
        angulo_grano_rad=angulo_vetas
    )
    
    # Inicialización del pipeline gráfico con Matplotlib
    plt.figure(figsize=(8, 6))
    
    # Renderizado del mapa de calor de tensiones elasto-plásticas (Gradiente Copper)
    plt.imshow(matriz_tension, cmap='copper', origin='upper')
    plt.colorbar(label='Intensidad de Tensión Estructural (Stress Tensor Approximation)')
    
    plt.title('Simulación de Impacto Anisotrópico: Restricciones Estructurales en Formas Sustractivas')
    plt.xlabel('Eje X (Planos de Desplazamiento Transversal)')
    plt.ylabel('Eje Y (Profundidad del Bloque / Eje de Carga)')
    
    # Superposición de vectores Quiver para denotar la dirección del tensor del material
    plt.quiver(
        30, 30, 
        np.cos(angulo_vetas) * 10, -np.sin(angulo_vetas) * 10, 
        scale=1, scale_units='xy', 
        color='cyan', label='Dirección del Grano (Veta Anisotrópica)'
    )
    plt.legend()
    
    print("[INFO] El mapa de tensiones topológicas ha sido generado y validado con éxito.")
    plt.show()
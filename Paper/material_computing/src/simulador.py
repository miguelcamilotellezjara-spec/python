import numpy as np

def simular_impacto_anisotropico(dimensiones=(60, 60), punto_impacto=(0, 30), fuerza=150, angulo_grano_rad=np.radians(30)):
    X, Y = dimensiones
    campo_tension = np.zeros(dimensiones)
    vector_grano = np.array([np.cos(angulo_grano_rad), np.sin(angulo_grano_rad)])
    
    for x in range(X):
        for y in range(Y):
            vector_distancia = np.array([x - punto_impacto[0], y - punto_impacto[1]])
            distancia = np.linalg.norm(vector_distancia)
            
            if distancia == 0:
                campo_tension[x, y] = fuerza
                continue
                
            direccion_impacto = vector_distancia / distancia
            alineacion_grano = np.abs(np.dot(direccion_impacto, vector_grano))
            
            atenuacion = 1.0 / (distancia ** 1.5)
            factor_anisotropico = 1.0 + 2.0 * alineacion_grano
            
            campo_tension[x, y] = fuerza * atenuacion * factor_anisotropico

    return campo_tension
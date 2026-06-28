import numpy as np

def verificar_limite_ruptura(matriz_tension, umbral_critico=12.0):
    """
    Actúa como un predicado lógico de verificación formal.
    Analiza si los tensores de estrés locales superan la resistencia elástica del material.
    """
    # Encontrar el punto de máxima tensión acumulada (excluyendo el impacto matemático puro)
    max_tension = np.max(matriz_tension[matriz_tension < np.max(matriz_tension)])
    
    # Contar cuántos elementos discretos (voxels/pixeles) han colapsado bajo la carga
    puntos_criticos = np.sum(matriz_tension > umbral_critico)
    total_elementos = matriz_tension.size
    porcentaje_dano = (puntos_criticos / total_elementos) * 100

    # Determinación formal del estado del sistema
    se_destruye = max_tension > umbral_critico

    analisis = {
        "max_tension": round(max_tension, 2),
        "porcentaje_dano": round(porcentaje_dano, 2),
        "se_destruye": se_destruye,
        "dictamen": "CRITICAL FAILURE: MATERIAL DESTROYED" if se_destruye else "STRUCTURE SECURE: MATERIAL RESISTED"
    }
    
    return analisis
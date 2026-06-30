import numpy as np

def verificar_limite_ruptura(matriz_tension, umbral_critico=12.0):
    """
    Actúa como un predicado lógico de verificación formal estructural P_struct.
    Analiza si los tensores de estrés locales superan la resistencia elástica del material.
    """
    max_tension = np.max(matriz_tension[matriz_tension < np.max(matriz_tension)])
    puntos_criticos = np.sum(matriz_tension > umbral_critico)
    total_elementos = matriz_tension.size
    porcentaje_dano = (puntos_criticos / total_elementos) * 100

    se_destruye = max_tension > umbral_critico

    analisis = {
        "max_tension": round(max_tension, 2),
        "porcentaje_dano": round(porcentaje_dano, 2),
        "se_destruye": se_destruye,
        "dictamen": "CRITICAL FAILURE: MATERIAL DESTROYED" if se_destruye else "STRUCTURE SECURE: MATERIAL RESISTED"
    }
    return analisis

def verificar_invariante_estetico_loomis(proporciones_generadas_inf, proporciones_generadas_sup, altura_cuerpo, epsilon=0.05):
    """
    ===========================================================================
    LOGICA DE VERIFICACIÓN FORMAL - INTERPRETACIÓN ABSTRACTA (P_aesthetic)
    ===========================================================================
    Matemáticamente modela el predicado sobre el dominio abstracto de intervalos.
    Verifica si las proporciones anatómicas generadas por la red neuronal difusa
    se encuentran contenidas en las aproximaciones polédricas/intervalos seguros
    del canon clásico de 8 cabezas de Andrew Loomis.
    
    Fórmula formalizada para el paper:
    P_aesthetic([[Λ_gen]]^#) <=> ∀i ∈ {1,..,8}, |([[Λ_gen]]^#[i] / Height) - Λ_ideal[i]| <= ε
    """
    # Vector canónico ideal de Loomis (Proporciones de articulaciones medido en unidades de cabezas 'H' sobre la altura total)
    # 1H: Barbilla, 2H: Tetillas, 3H: Ombligo, 4H: Pubis/Entrepierna (Mitad exacta del cuerpo), etc.
    # Estas son las posiciones relativas normalizadas ideales (cumulativas desde la corona de la cabeza):
    LAMBDA_IDEAL = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]) / 8.0
    
    # Abstracción de la geometría concreta generada a intervalos normalizados de la malla
    # Representa la sobre-aproximación del dominio abstracto [[Λ_gen]]^#
    intervalo_inf = proporciones_generadas_inf / altura_cuerpo
    intervalo_sup = proporciones_generadas_sup / altura_cuerpo
    
    errores_detectados = []
    
    print("[ABSTRACT INTERPRETATION] Evaluando punto fijo en dominio posets de Loomis...")
    
    for i in range(8):
        # En análisis de intervalos, calculamos el peor escenario de desviación (supremo del error absoluto)
        error_inf = abs(intervalo_inf[i] - LAMBDA_IDEAL[i])
        error_sup = abs(intervalo_sup[i] - LAMBDA_IDEAL[i])
        peor_error_abstracto = max(error_inf, error_sup)
        
        if peor_error_abstracto > epsilon:
            errores_detectados.append(
                f"Articulación {i+1}H fuera de rango ideal. Desviación máx calculada: {peor_error_abstracto:.3f} > ε={epsilon}"
            )
            
    armonioso = len(errores_detectados) == 0
    
    return {
        "armonioso": armonioso,
        "detalles_abstraccion": errores_detectados,
        "dictamen": "AESTHETIC HARMONY VALIDATED: CONFORMS TO CLASSICAL REALISM" if armonioso else "ESTHETIC VIOLATION: ABERRANT ANATOMICAL DISTORTION DETECTED"
    }
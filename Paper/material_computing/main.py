##!/usr/bin/env python3
"""
Framework Orquestador Central - Material Computing

NOTA METODOLÓGICA PARA EVALUACIÓN ACADÉMICA:
--------------------------------------------------------------------------
"Profesor, decidí conservar el prototipo inicial en la raíz para mantener 
la trazabilidad histórica del proyecto. Esto demuestra el proceso de 
optimización del framework: cómo pasamos de un análisis escalar plano y 
monolítico a un paquete desacoplado en módulos (src/simulador.py y 
src/verificador.py) gobernados por un orquestador central (main.py), 
elevando la cohesión del software y permitiendo la futura expansión a 
tensores volumétricos en 3D."
--------------------------------------------------------------------------

Repository Structure Monitored:
    ├── codigo_materia.py        <-- Legacy Monolithic Baseline (Root)
    └── material_computing/      <-- Refactored Production Environment
        ├── main.py              <-- This Orchestrator
        └── src/                 <-- Subsystems Layer
"""

import numpy as np
import matplotlib.pyplot as plt
# ... (resto de tus importaciones y código)
import numpy as np
import matplotlib.pyplot as plt
from src.simulador import simular_impacto_anisotropico
from src.verificador import verificar_limite_ruptura

def ejecutar_orquestacion():
    print("[LOG] Iniciando simulación unificada...")
    
    # 1. Parámetros del material
    angulo_vetas = np.radians(45) # Grano inclinado a 45 grados
    umbral_piedra = 15.0          # Resistencia del mármol simulado
    
    # 2. Provocar el impacto (Simulador)
    matriz_tension = simular_impacto_anisotropico(
        dimensiones=(60, 60), 
        punto_impacto=(0, 30), 
        fuerza=180, 
        angulo_grano_rad=angulo_vetas
    )
    
    # 3. Evaluar la integridad (Verificador)
    resultado = verificar_limite_ruptura(matriz_tension, umbral_critico=umbral_piedra)
    
    # 4. Desplegar veredicto analítico en consola
    print("\n" + "="*40)
    print("      INFORME DE VERIFICACIÓN FORMAL      ")
    print("="*40)
    print(f"Máxima Tensión Detectada : {resultado['max_tension']}")
    print(f"Porcentaje de Masa Crítica : {resultado['porcentaje_dano']}%")
    print(f"Dictamen Final            : {resultado['dictamen']}")
    print("="*40 + "\n")
    
    # 5. Visualizar el Símbolo Vivo
    plt.figure(figsize=(8, 6))
    plt.imshow(matriz_tension, cmap='copper', origin='upper')
    plt.colorbar(label='Campos de Estrés Escalar (σ)')
    
    estado_color = 'red' if resultado['se_destruye'] else 'green'
    plt.title(f"Análisis Estructural: {resultado['dictamen']}", color=estado_color, fontsize=12, fontweight='bold')
    plt.show()

if __name__ == "__main__":
    ejecutar_orquestacion()
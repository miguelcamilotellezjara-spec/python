# 3. Ejemplo Práctico Paso a Paso: El Sistema de un Termostato
#Imagina que estás modelando un dispositivo de control de temperatura. 
#El termostato no puede configurarse a menos de 0°C ni a más de 100°C porque dañaría el equipo.
## Paso 1 y 2: Formular la excepción personalizada
class TemperaturaFueraDeRangoError(Exception):
    """Excepción lanzada cuando la temperatura asignada supera los límites seguros."""
    def __init__(self, temperatura_intentada, mensaje="La temperatura está fuera de los límites de seguridad (0°C - 100°C)."):
        self.temperatura_intentada = temperatura_intentada
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f"¡Operación Rechazada! {self.mensaje} | Intentaste asignar: {self.temperatura_intentada}°C"

## Paso 3: Lanzar la excepción dentro de los métodos de la clase
class Termostato:
    def __init__(self, ubicacion, temperatura_inicial=20):
        self.ubicacion = ubicacion
        # Usamos el método de validación incluso al inicializar
        self.temperatura = self.configurar_temperatura(temperatura_inicial)

    def configurar_temperatura(self, nueva_temp):
        # 1. Validaciones básicas de tipo de dato (Buenas prácticas)
        if not isinstance(nueva_temp, (int, float)):
            raise TypeError("La temperatura debe ser un valor numérico.")
            
        # 2. Validación de estado del objeto usando nuestra excepción
        if nueva_temp < 0 or nueva_temp > 100:
            # Lanzamos nuestra excepción e inyectamos el dato fallido
            raise TemperaturaFueraDeRangoError(nueva_temp)
            
        self.temperatura = nueva_temp
        print(f"[{self.ubicacion}] Temperatura ajustada con éxito a {self.temperatura}°C.")
        return self.temperatura
    
## Paso 4: Probar e integrar el control de flujo
# --- Simulando el comportamiento del sistema ---
if __name__ == "__main__":
    mi_termostato = Termostato("Sala Principal", 22)

    # Intento de configuración inválido
    try:
        print("\nIntentando subir la temperatura a un nivel peligroso...")
        mi_termostato.configurar_temperatura(150) # Esto disparará el raise
        
    except TemperaturaFueraDeRangoError as e:
        # Aquí capturamos específicamente nuestro error y accedemos a su __str__
        print(f"Control de Riesgos -> {e}")
        
    except TypeError as e:
        print(f"Error de Entrada -> {e}")
        
    finally:
        print(f"\n[Monitoreo] Estado actual del termostato: {mi_termostato.temperatura}°C. Sistema estable.")
    

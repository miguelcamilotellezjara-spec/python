# TRY ! EXCEPT ! ELSE ! FINALLY

# Programa que se encarga de multiplicar dos números (Dará error y el programa se bloqueará, no queremos eso)
numero = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

resultado = numero * numero2
print("El resultado de la multiplicación es: ", resultado)

# Solución con las sentencias try y except: 

try:
    numero = int(input("Introduce un número: "))
    numero2 = int(input("Introduce otro número: "))

    resultado = numero * numero2
    print("El resultado de la multiplicación es: ", resultado)  
except:
    print("Debes introducir un número, no funciona si pones otra cosa")
          
# Sentencia finally (se ejecuta si ó si)

try:
    numero = int(input("Introduce un número: "))
    numero2 = int(input("Introduce otro número: "))

    resultado = numero * numero2
    print("El resultado de la multiplicación es: ", resultado)
except:
    print("Debes introducir un número, no funciona si pones otra cosa")
finally:
    print("Esto se imprime de ley: Gracias por usar el programa")

# Control de las excepciones usando un bucle while:

while (True):
    try:
        numero = int(input("Introduce un número: "))
        numero2 = int(input("Introduce otro número: "))

        resultado = numero * numero2
        print("El resultado de la multiplicación es: ", resultado)
        break
    except:
        print("Debes introducir números, vuelve a intentarlo")

# Código fuente de try-except en Python:
try:
    # Código que puede fallar
    resultado2 = 10 / 0
except ZeroDivisionError:
    # Manejo del error
    print ("¡Error: División por cero!")

# 7 Múltiples Excepciones Comunes
#FileNotFoundError: Ocurre cuando se intenta abrir un archivo que no existe.
#ValueError: Ocurre cuando se intenta convertir un valor a un tipo de dato que no es compatible.
#TypeError: Ocurre cuando se intenta realizar una operación con tipos de datos incompatibles.        
#KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
#IndexError: Ocurre cuando se intenta acceder a un índice que está fuera del rango de una lista o tupla
#AttributeError: Ocurre cuando se intenta acceder a un atributo que no existe en un objeto POO.
#ZeroDivisionError: Ocurre cuando se intenta dividir un número por cero.

# Excepciones Personalizadas
class SaldoInsuficienteError(Exception):
    """Excepción personalizada para saldo insuficiente."""
    pass

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial  
    
    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficienteError("Saldo Insuficiente") #Comentar siempre Excepción personalizada. 
        self.saldo -= monto
        return self.saldo

#Uso
try:
    cuenta = CuentaBancaria(100)
    cuenta.retirar(200)
except SaldoInsuficienteError as e:
    print(f"Error: {e}")

# Código fuente de múltiples excepciones en Python
try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
    lista = [1, 2, 3]
    print(lista[10])
except ValueError:  
    print("¡Debe ingresar un número válido!")
except ZeroDivisionError:
    print("¡División por cero!")
except IndexError:
    print("¡Índice fuera de rango!")
except Exception as e: #Captura cualquier otro error
    print(f"Error inesperado: {e}")

# Bloque else (se ejecuta si no hay excepciones)
#else: repito se ejecuta si no hubo excepciones
#finally: repito se ejecuta de ley, si o si, siempre se ejecuta, útil para liberar recursos.

#Código fuente de lectura de archivos en Python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("¡Archivo no encontrado!")    
else:
    print("Lectura exitosa.")
    print(contenido)
finally:
    archivo.close() if "archivo" in locals() else None
    print("Proceso finalizado. Archivo cerrado.")

#Buenas Prácticas con Excepciones
#1.Usa excepciones específicas en lugar de Exception genérico.
#2.Documenta tus excepciones personalizadas con docstrings.
#3.Evita try-except demasiado amplios, solo captura lo necesario.
#4. Usa finally para liberar recursos, archivos, conexiones a BD.

#Más Ejemplos De GitHub
#Calculadora.py
class Calculadora:
    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "¡No se puede dividir por cero!"
        except TypeError:
            return "¡Entradas deben ser números!"

calc = Calculadora()

print(calc.dividir(10, 0))  # ¡No se puede dividir por cero!
print(calc.dividir("10", 2))  # ¡Entradas deben ser números!

#Entradas.py
class Validador:
    @staticmethod
    def validar_edad(edad):
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número.")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        return True

try:
    Validador.validar_edad("25")  # Error: no es int
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

#Explicación Detallada "e"
#except (TypeError, ValueError) as e:
    #print(f"Error: {e}")

#"e" no es mas que una variable donde se guarda el error que acaba de pasar
# y luego lo imprime con una cadena de texto, en este caso "Error: " y luego el error que se acaba de pasar.
#Sintesis: e solo es una variable que guarda TypeErrors o ValueErrors. . .
#luego en print e se imprime el error con la cadena.

#PREPARACIÓN 
# ==============================================================================
# 1. CREACIÓN DE EXCEPCIONES PERSONALIZADAS PARA VALIDAR ESTADOS DE OBJETOS
# ==============================================================================

class SaldoInsuficienteError(Exception):
    """
    Excepción personalizada para controlar el estado de una cuenta bancaria
    cuando se intenta realizar un retiro mayor al saldo disponible.
    """
    def __init__(self, saldo_actual, monto_retiro, mensaje="Saldo insuficiente para realizar la operación."):
        self.saldo_actual = saldo_actual
        self.monto_retiro = monto_retiro
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f"{self.mensaje} | Saldo disponible: {self.saldo_actual} | Intento de retiro: {self.monto_retiro}"


# ==============================================================================
# 2. BLOQUES TRY, EXCEPT, FINALLY DENTRO DE MÉTODOS DE CLASE
# ==============================================================================

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria y demuestra el uso de control de excepciones,
    validaciones de tipo de dato y gestión de recursos dentro de sus métodos.
    """
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial  
    
    def retirar(self, monto):
        """
        Método que valida el estado del objeto antes de modificarlo y utiliza
        excepciones específicas para mantener la integridad del sistema.
        """
        # Buena práctica 1: Validar tipos de datos de forma específica antes de operar
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto del retiro debe ser un número entero o decimal.")
        
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero.")

        # Validación del estado del objeto usando la excepción personalizada
        if monto > self.saldo:
            raise SaldoInsuficienteError(self.saldo, monto)
            
        self.saldo -= monto
        return self.saldo

    def generar_reporte_transaccion(self, nombre_archivo):
        """
        Demostración del uso de bloques try-except-else-finally dentro de un método
        de clase para la lectura/escritura de archivos (Manejo seguro de recursos).
        """
        archivo = None
        try:
            # Intentamos abrir un archivo para registrar o simular la persistencia
            archivo = open(nombre_archivo, "w")
            archivo.write(f"Reporte de Transacción\nTitular: {self.titular}\nSaldo Final: {self.saldo}\n")
        
        except FileNotFoundError:
            print(f"¡Error! No se encontró la ruta o el archivo: {nombre_archivo}")
            
        except PermissionError:
            print(f"¡Error de permisos! No se puede escribir en: {nombre_archivo}")
            
        else:
            # Se ejecuta únicamente si el bloque 'try' no arrojó ningún error
            print("El reporte físico se generó y escribió de manera exitosa.")
            
        finally:
            # Buena práctica 4: El bloque 'finally' garantiza el cierre del recurso, pase lo que pase
            if archivo and not archivo.closed:
                archivo.close()
                print("Recurso liberado: Archivo cerrado correctamente en la cláusula 'finally'.")


# ==============================================================================
# 3. DEMOSTRACIÓN DE USO Y BUENAS PRÁCTICAS EN EL MANEJO DE EXCEPCIONES
# ==============================================================================

if __name__ == "__main__":
    print("--- INICIO DE LAS PRUEBAS DE INTEGRIDAD DEL SISTEMA ---")
    
    # Instanciamos el objeto con un saldo inicial de 100
    cuenta_miguel = CuentaBancaria("Miguel Téllez", 100)

    # Caso 1: Captura de Excepción Personalizada (Validación de Estado del Objeto)
    try:
        print(f"\nIntentando retirar 200 de la cuenta de {cuenta_miguel.titular}...")
        cuenta_miguel.retirar(200)
    except SaldoInsuficienteError as e:
        # Aquí 'e' es la instancia de nuestra excepción personalizada
        print(f"Manejo Explicito -> {e}")

    # Caso 2: Captura de Múltiples Excepciones Específicas (Tipos de datos incorrectos)
    try:
        print("\nIntentando pasar una cadena de texto como monto de retiro...")
        cuenta_miguel.retirar("doscientos pesos")
    except TypeError as e:
        print(f"Manejo Explicito de Tipo -> Error: {e}")
    except ValueError as e:
        print(f"Manejo Explicito de Valor -> Error: {e}")

    # Caso 3: Ejecución de try-except-else-finally dentro del método de clase
    print("\nEjecutando método con persistencia de archivos y bloque finally:")
    cuenta_miguel.generar_reporte_transaccion("estado_cuenta.txt")

    
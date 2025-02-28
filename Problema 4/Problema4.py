def calcular_separacion(t, d0, a1, a2):
    """ Calcula la separación entre los carritos después de un tiempo t. """
    x1 = 0.5 * a1 * (t ** 2)
    x2 = 0.5 * a2 * (t ** 2)
    separacion = d0 - (x1 + x2)
    return separacion

def calcular_tiempo_encuentro(d0, a1, a2):
    """ Calcula el tiempo en el que los carritos se encuentran. """
    if a1 + a2 == 0:
        return None  # Evita división por cero
    t = (2 * d0 / (a1 + a2)) ** 0.5
    return t

def validar_flotante(mensaje):
    """ Solicita y valida la entrada de un número flotante. """
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Ingrese un número.")

def main():
    print("\nBienvenido al programa de simulación de carritos en MRUA.")
    print("Este programa calcula la separación entre dos carritos que parten con aceleraciones distintas y determina el tiempo en que se encuentran.")

    while True:
        # Solicitar datos con validaciones
        d0 = validar_flotante("\nIngrese la distancia inicial entre los carritos (en metros): ")
        a1 = validar_flotante("Ingrese la aceleración del carrito 1 (en m/s²): ")
        a2 = validar_flotante("Ingrese la aceleración del carrito 2 (en m/s²): ")
        t = validar_flotante("Ingrese el tiempo a evaluar (en segundos): ")

        # Calcular separación después de t segundos
        separacion = calcular_separacion(t, d0, a1, a2)
        print(f"\nDespués de {t} segundos, la separación entre los carritos es de {separacion:.2f} metros.")

        # Calcular tiempo de encuentro
        tiempo_encuentro = calcular_tiempo_encuentro(d0, a1, a2)
        if tiempo_encuentro is not None:
            print(f"Los carritos se encuentran después de aproximadamente {tiempo_encuentro:.2f} segundos.")
        else:
            print("No es posible calcular el tiempo de encuentro con las aceleraciones dadas.")

        # Preguntar si el usuario desea repetir
        repetir = input("\n¿Desea realizar otro cálculo? (s/n): ").strip().lower()
        if repetir != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()

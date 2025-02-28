import time

def validar_flotante(mensaje):
    """Solicita un número flotante positivo al usuario y valida la entrada."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor ingrese un valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Ingrese un número positivo.")


def validar_entero(mensaje):
    """Solicita un número entero positivo al usuario y valida la entrada."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Por favor ingrese un valor entero positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")


def dibujar_tren(distancia, escala=0.1, ancho=50):
    """
    Dibuja el tren como 'T' sobre una pista representada por '.'.
    - 'distancia' es la distancia recorrida en metros.
    - 'escala' convierte metros a cantidad de caracteres.
    - 'ancho' es la longitud máxima de la pista en caracteres.
    """
    posicion = int(distancia * escala)
    if posicion > ancho:
        posicion = ancho  # Evita salirse de la pantalla

    pista = '.' * (posicion) + 'T'
    if posicion < ancho:
        pista += '.' * (ancho - posicion)
    print(pista)


def simular_tren():
    """
    Simula el recorrido del tren en 3 fases:
    1. Desaceleración hasta velocidad 0.
    2. Parada en la estación.
    3. Aceleración hasta la velocidad inicial.
    Muestra en consola el estado y una mini-animación de la posición.
    """
    print("\n--- Simulación del tren con mini-animación ---")

    # Solicitar datos al usuario con validaciones
    v_inicial = validar_flotante("Ingrese la velocidad inicial del tren (m/s): ")
    tiempo_parada = validar_entero("Ingrese el tiempo de parada en la estación (segundos): ")
    desac = -validar_flotante("Ingrese la magnitud de la desaceleración (m/s^2): ")
    acel = validar_flotante("Ingrese la aceleración (m/s^2): ")
    dt = validar_flotante("Ingrese el intervalo de tiempo para la simulación (segundos): ")
    if dt <= 0:
        dt = 1  # Por seguridad, evitamos dt=0 o negativo

    # Impresión de datos iniciales
    print(f"\nVelocidad inicial: {v_inicial} m/s")
    print(f"Desaceleración: {desac} m/s^2")
    print(f"Aceleración: {acel} m/s^2")
    print(f"Tiempo de parada en estación: {tiempo_parada} s")
    print(f"Intervalo de simulación: {dt} s")
    print("-------------------------------------------------\n")

    # -------------------
    # FASE 1: Desaceleración
    # -------------------
    print("FASE 1: Desaceleración")
    v = v_inicial  # velocidad actual
    t = 0.0  # tiempo transcurrido
    x = 0.0  # distancia recorrida

    while v > 0:
        # Mostrar estado actual
        print(f"Tiempo: {t:6.2f} s | Velocidad: {v:6.2f} m/s | Estado: Desacelerando", end=" | ")
        dibujar_tren(x)

        # Actualizar movimiento (simple integración paso a paso)
        x += v * dt
        v += desac * dt
        if v < 0:
            v = 0  # Evitar pasar a velocidad negativa
        t += dt

        # Espera para "animación"
        time.sleep(0.2)

    # -------------------
    # FASE 2: Parada
    # -------------------
    print("\nFASE 2: Parada en estación")
    tiempo_parado = 0
    while tiempo_parado < tiempo_parada:
        # Mostrar tren detenido
        print(f"Tiempo: {t:6.2f} s | Velocidad: {0:6.2f} m/s | Estado: EN ESTACIÓN", end=" | ")
        dibujar_tren(x)

        tiempo_parado += dt
        t += dt
        time.sleep(0.2)

    # -------------------
    # FASE 3: Aceleración
    # -------------------
    print("\nFASE 3: Aceleración")
    v = 0
    while v < v_inicial:
        # Mostrar estado actual
        print(f"Tiempo: {t:6.2f} s | Velocidad: {v:6.2f} m/s | Estado: Acelerando", end=" | ")
        dibujar_tren(x)

        # Actualizar movimiento
        x += v * dt
        v += acel * dt
        if v > v_inicial:
            v = v_inicial
        t += dt
        time.sleep(0.2)

    # Estado final
    print(f"\nTiempo: {t:6.2f} s | Velocidad: {v_inicial:6.2f} m/s | Estado: Velocidad Recuperada", end=" | ")
    dibujar_tren(x)
    print("\nEl tren ha completado la simulación.\n")


def main():
    print("Bienvenido a la simulación del tren (Problema 5 - Parte EXTRA).")
    print("En esta simulación, el tren se desacelera hasta detenerse,")
    print("permanece un tiempo en la estación y luego vuelve a acelerar.")
    print("Se muestra una animación aproximada en consola. ¡Disfruta!\n")

    # Ejecutar simulación
    simular_tren()

    print("Gracias por usar el programa. ¡Hasta luego!")


if __name__ == "__main__":
    main()

# Problema 1b - Calcula el tiempo que tarda un impulso nervioso según la altura ingresada
print("Este programa calcula el tiempo que tarda un impulso nervioso en llegar al cerebro.")
print("Se usa la altura ingresada (en metros) y se estima la distancia como el 90% de esa altura.")
print("La velocidad del impulso es 100 m/s.")

while True:
    try:
        altura = float(input("Ingrese la altura de la persona (ej: 1.70): "))
        if altura < 0:  # Validación para altura negativa
            print("¡Error! La altura no puede ser negativa. Intente de nuevo.")
        elif altura <= 0.5:  # Validación para alturas absurdamente bajas
            print("¡Error! Esa altura es muy baja para una persona. Ingrese algo razonable.")
        else:
            distancia = altura * 0.9  # Distancia efectiva del dedo del pie al cerebro
            velocidad = 100  # m/s
            tiempo = distancia / velocidad
            print(f"El tiempo que tarda el impulso es: {tiempo:.4f} s")

        # Pregunta para continuar
        while True:
            continuar = input("¿Quiere calcular otra altura? (sí/no): ").lower()
            if continuar in ['sí', 'si', 's']:
                break  # Vuelve al inicio del ciclo
            elif continuar in ['no', 'n']:
                print("¡Programa terminado!")
                exit()  # Termina el programa
            else:
                print("Por favor, responda 'sí' o 'no'.")

        print("-----------------------------------")
    except ValueError:  # Validación para entradas no numéricas
        print("¡Error! Ingrese un número válido, por favor.")
        print("-----------------------------------")
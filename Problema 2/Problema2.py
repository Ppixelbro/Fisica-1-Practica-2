# Problema 2b - Calcula el tiempo hasta el siguiente corte de cabello usando MRU
print("Este programa calcula el tiempo hasta el siguiente corte de cabello con MRU.")
print("Ingrese la longitud inicial y final (en cm) y elija la unidad de tiempo.")
print("La tasa de crecimiento es 2 cm/mes.")

while True:
    try:
        long_inicial = float(input("Ingrese la longitud inicial del cabello (en cm): "))
        if long_inicial < 0:
            print("¡Error! La longitud inicial no puede ser negativa. Intente de nuevo.")
            continue

        long_final = float(input("Ingrese la longitud final deseada (en cm): "))
        if long_final < 0:
            print("¡Error! La longitud final no puede ser negativa. Intente de nuevo.")
            continue
        elif long_final <= long_inicial:
            print("¡Error! La longitud final debe ser mayor que la inicial. Intente de nuevo.")
            continue

        unidad = int(input("Elija la unidad de tiempo (1: meses, 2: días, 3: semanas): "))
        tasa = 2  # cm/mes por defecto (velocidad en MRU)
        if unidad == 1:
            tasa = 2  # cm/mes
            unidad_str = "meses"
        elif unidad == 2:
            tasa = 2 / 30  # cm/día (aproximando 30 días por mes)
            unidad_str = "días"
        elif unidad == 3:
            tasa = 2 / 4.33  # cm/semana (aproximando 4.33 semanas por mes)
            unidad_str = "semanas"
        else:
            print("¡Error! Ingrese 1, 2 o 3 para la unidad de tiempo. Intente de nuevo.")
            continue

        distancia = long_final - long_inicial  # "Distancia" en MRU
        tiempo = distancia / tasa  # Tiempo usando la fórmula de MRU
        print(f"El tiempo hasta el siguiente corte es: {tiempo:.2f} {unidad_str}")

        # Pregunta para continuar
        while True:
            continuar = input("¿Quiere calcular otro caso? (sí/no): ").lower()
            if continuar in ['sí', 'si', 's']:
                break
            elif continuar in ['no', 'n']:
                print("¡Programa terminado!")
                exit()
            else:
                print("Por favor, responda 'sí' o 'no'.")

        print("-----------------------------------")
    except ValueError:
        print("¡Error! Ingrese un número válido, por favor.")
        print("-----------------------------------")
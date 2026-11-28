
# Escenario 2: Dosificacion de presion en red de gas natural
# Transductor XMLP010BC71F

def controlar_presion():
    # Valor inicial ilustrativo para la simulacion, en bar.
    presion_bar = 1.5

    for lectura in range(10):
        print(f"Lectura {lectura + 1}: {presion_bar:.2f} bar")

        if presion_bar >= 6.0:
            print("CRITICO: Ruptura inminente. Abortar.")
            break

        if presion_bar < 2.0:
            print("Accion: Inyectando presion a la red")
            presion_bar += 0.5

        elif 2.0 <= presion_bar <= 4.5:
            print("Accion: Flujo nominal estabilizado")
            presion_bar += 0.1

        else:
            print("Accion: Purga de emergencia abierta")
            presion_bar -= 0.8


if __name__ == "__main__":
    controlar_presion()

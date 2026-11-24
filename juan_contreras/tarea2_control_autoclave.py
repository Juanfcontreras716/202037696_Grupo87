temperatura = 100 # °C
sistema_activo = True

while sistema_activo:
    if temperatura > 130:
        print("ALERTA CRÍTICA: Parada de emergencia")
        sistema_activo = False
    elif temperatura < 115:
        print("Estado: Calentando autoclave")
        temperatura += 2
    elif temperatura >= 115 and temperatura <= 121:
        print("Estado: Fase estable de esterilización")
        temperatura += 1
    else:
        print("Estado: Enfriamiento activo")
        temperatura -= 3

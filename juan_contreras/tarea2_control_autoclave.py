"""Control de temperatura de un autoclave (sensor MAX31855)."""

TEMPERATURA_INICIAL = 100  # grados Celsius
MAX_LECTURAS = 20

temperatura = TEMPERATURA_INICIAL
sistema_activo = True
lecturas = 0

while sistema_activo and lecturas < MAX_LECTURAS:
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
    lecturas += 1

if sistema_activo:
    print(f"Simulación finalizada: {MAX_LECTURAS} lecturas completadas")

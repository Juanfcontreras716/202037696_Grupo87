registro_mpu = {
    "0x3B": {
        "register_name": "ACCEL_XOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000
    },
    "0x3D": {
        "register_name": "ACCEL_YOUT_H",
        "bit_mask": 0xE0,
        "sampling_rate": 1000
    },
    "0x6B": {
        "register_name": "PWR_MGMT_1",
        "bit_mask": 0x40,
        "sampling_rate": 100
    }
}

MAX_INTENTOS = 5
intentos = 0

while intentos < MAX_INTENTOS:
    consulta = input("Dirección hex (ej. 0x3B) o nombre de registro ('salir' para terminar): ").strip()
    if consulta.lower() == "salir":
        break
    intentos += 1
    clave = consulta.upper().replace("0X", "0x")

    direccion = clave
    datos = registro_mpu.get(clave)
    if datos is None:
        for dir_hex, info in registro_mpu.items():
            if info.get("register_name") == clave:
                direccion = dir_hex
                datos = info
                break

    if datos is None:
        print(f"Registro '{consulta}' no encontrado. Intentos restantes: {MAX_INTENTOS - intentos}")
    else:
        print(f"Dirección:      {direccion}")
        print(f"Registro:       {datos.get('register_name', 'N/D')}")
        print(f"Máscara de bits: 0x{datos.get('bit_mask', 0):02X}")
        print(f"Frecuencia:     {datos.get('sampling_rate', 'N/D')} Hz")
else:
    print("Límite de consultas alcanzado.")

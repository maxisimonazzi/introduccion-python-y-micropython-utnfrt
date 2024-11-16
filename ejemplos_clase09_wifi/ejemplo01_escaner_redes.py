import network

# Inicializar la interfaz de estación
# STA_IF: Station Interface
# AP_IF: Access Point Interface
estacion = network.WLAN(network.STA_IF)

# Activar la interfaz de estación
estacion.active(True)

# Escanear las redes disponibles
redes = estacion.scan()

print(redes)

# Desactivar la interfaz de estación
estacion.active(False)
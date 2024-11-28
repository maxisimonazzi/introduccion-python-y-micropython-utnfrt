from machine import Pin
from conector_wifi import ConectorWIFI
from time import sleep
from urequests import get

# Configurar el pin GPIO 2 como salida (LED incorporado)
led = Pin(2, Pin.OUT)
led.off()

# Configurar el pin GPIO 0 para el botón BOOT como entrada
button = Pin(0, Pin.IN)

def main():
    wifi = ConectorWIFI()
    wifi_connect = wifi.wifi_connect("WifiConector", "wificonector")
    wifi.show_message("Iniciando WiFi...", line=1)
    sleep(2)
    
    estado_led = False  # False = apagado, True = encendido
    ultimo_estado_boton = button.value()
    
    while True:
        try:
            if not wifi_connect:
                wifi.show_message("Error conexion", line=1)
                led.off()
                sleep(1)
                continue
            
            estado_actual = button.value()
            if estado_actual == 0 and ultimo_estado_boton == 1:  # Detecta cuando se presiona el botón
                estado_led = not estado_led  # Cambia el estado
                url = f"http://192.168.4.1/?led={'on' if estado_led else 'off'}"
                
                for _ in range(3):  # Intentar la petición GET hasta 3 veces
                    try:
                        response = get(url)
                        if response.status_code == 200:
                            mensaje = "LED encendido" if estado_led else "LED apagado"
                            wifi.show_message(mensaje, line=1)
                            led.value(estado_led)  # Actualiza LED local
                            response.close()
                            break
                        response.close()
                    except Exception as e:
                        wifi.show_message(f"Reintentando... {str(e)}", line=1)
                        sleep(1)
            
            ultimo_estado_boton = estado_actual
            sleep(0.1)  # Debounce delay
        except Exception as e:
            wifi.show_message(f"Error inesperado: {str(e)}", line=1)
            sleep(1)

if __name__ == '__main__':
    main()

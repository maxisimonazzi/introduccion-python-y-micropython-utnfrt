from machine import Pin, ADC, PWM, SoftI2C
from time import sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import network
import socket
import urequests


################################## WI_Fi ##############################################
#Configuracion para la conexion de la placa a la red
ssid='tu_red_wifi'
password='tu_contraseña'
estacion=network.WLAN(network.STA_IF)
estacion.active(True)
estacion.connect(ssid, password)

# Configuración del Access Point
ap = network.WLAN(network.AP_IF)
ap.active(True)
nombre = 'Mi_ESP32_AP'
contrasena = '1234567890'
ap.config(essid=nombre, password=contrasena, authmode=network.AUTH_WPA_WPA2_PSK)
ip = '10.0.0.15'
mascara_subred = '255.255.255.0'
puerta_enlace = '10.0.0.15'
dns = '10.0.0.15'
ap.ifconfig((ip, mascara_subred, puerta_enlace, dns))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 80))
s.listen(5)
s.setblocking(False)
#######################################################################################


#Definiciones de pines y obejeto pantalla
i2c=SoftI2C(sda=Pin(25), scl=Pin(26), freq=1000)
pantalla = I2cLcd(i2c, 0x27, 2, 16)

#Definición de salidas para el led
led_R=PWM(Pin(21))
led_G=PWM(Pin(19))
led_B=PWM(Pin(18))

led_R.freq(1000)
led_G.freq(1000)
led_B.freq(1000)

#Definición de salidas para el led por via web
ledweb_R=PWM(Pin(4))
ledweb_G=PWM(Pin(2))
ledweb_B=PWM(Pin(15))

ledweb_R.freq(1000)
ledweb_G.freq(1000)
ledweb_B.freq(1000)

#Definición de entrada de potenciometros
pot_R = ADC(Pin(34))
pot_G = ADC(Pin(35))
pot_B = ADC(Pin(32))

#Ancho del bit de lectura (1024)
pot_R.width(ADC.WIDTH_10BIT)
pot_G.width(ADC.WIDTH_10BIT)
pot_B.width(ADC.WIDTH_10BIT)

#Atenuación de entrada de medición para valores de 3.3V
pot_R.atten(ADC.ATTN_11DB)
pot_G.atten(ADC.ATTN_11DB)
pot_B.atten(ADC.ATTN_11DB)



################################### MAIN ##############################################

#Verificacion de la conexion a la red
pantalla.clear()
pantalla.move_to(0,0)
pantalla.putstr('Conectando ...')
while not estacion.isconnected():
    pantalla.move_to(0,1)
    pantalla.putstr('Esperando')
    sleep(0.1)

pantalla.move_to(0,1)
pantalla.putstr('Conectado')
sleep(2)


while True:
    R=pot_R.read()
    G=pot_G.read()
    B=pot_B.read()
    led_R.duty(1023-R)
    led_G.duty(1023-G)
    led_B.duty(1023-B)

    pantalla.clear()
    pantalla.move_to(2,0)
    pantalla.putstr(f'R:{R/4:.0f}')
    pantalla.move_to(8,0)
    pantalla.putstr(f'G:{G/4:.0f}')
    pantalla.move_to(2,1)
    pantalla.putstr(f'B:{B/4:.0f}')
    
    # Parsear parámetros RGB
    try:
        cliente, ip_cliente = s.accept()
        request = cliente.recv(1024).decode()
        
        if 'GET /?' in request:
            params = request.split(' ')[1].split('?')[1]
            param_dict = {p.split('=')[0]: int(p.split('=')[1]) for p in params.split('&')}
            RWEB = param_dict.get('r', 0) * 4
            GWEB = param_dict.get('g', 0) * 4
            BWEB = param_dict.get('b', 0) * 4
            print(f"Color recibido: R={RWEB}, G={GWEB}, B={BWEB}")
            ledweb_R.duty(1023 - RWEB)
            ledweb_G.duty(1023 - GWEB)
            ledweb_B.duty(1023 - BWEB)
        
        cliente.close()
    except OSError:
        pass
    
    sleep(0.75)


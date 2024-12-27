from machine import Pin, PWM
import socket
import network
from time import sleep

servo = PWM(Pin(15))  
servo.freq(50)  

def mover_servo(angulo):
    min_duty = 2000  
    max_duty = 8000  
    duty = min_duty + int((angulo / 180) * (max_duty - min_duty))
    servo.duty_u16(duty)

mover_servo(140)

ssid = "wifi"
password = "contraseña"
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print("Conectado a Wi-Fi")
print(station.ifconfig())

html = """<!DOCTYPE html>
<html>
    <head>
        <title>comedero automatico</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #4CAF50;
                margin-top: 20px;
            }
            p {
                font-size: 18px;
                margin: 20px 0;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                font-size: 16px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>comedero automatico</h1>
        <p>Presiona el boton para alimentar a kira:</p>
        <form action="/mover">
            <button type="submit"> alimentar </button>
        </form>
    </body>
</html>
"""


addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Servidor en ejecución")

while True:
    cl, addr = s.accept()
    print(f"Conexión desde {addr}")
    request = cl.recv(1024)
    request = str(request)
    print(f"Solicitud: {request}")

    
    if "GET /mover" in request:
        mover_servo(50)
        sleep(2)
        mover_servo(140)

  
    cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
    cl.send(html)
    cl.close()

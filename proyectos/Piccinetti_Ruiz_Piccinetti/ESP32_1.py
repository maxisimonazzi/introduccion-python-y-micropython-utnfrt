from machine import Pin
from time import sleep
from conector_wifi import ConectorWIFI

# Configurar el pin del LED
led = Pin(5, Pin.OUT)

class CustomWebServer:
    def __init__(self):
        # Inicializar la conexión WiFi
        self.wifi = ConectorWIFI()
        self.wifi.show_message("OLED-WIFI")
        
    def web_html(self):
        """Genera la página web completa"""
        return """
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <title>ESP32 WEB</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <meta charset="UTF-8">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        background-color: #f0f0f0;
                    }
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                        background-color: white;
                        border-radius: 10px;
                        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    }
                    h1 {
                        color: #333;
                        text-align: center;
                    }
                   .btn {
                            background-color: #04AA6D; /* verde */
                            border: none;
                            color: white;
                            padding: 15px 32px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Control de LED</h1>
                     <form action="/?" method="get">
                    <input type="submit" class="btn" name="led" value="on">
                    <input type="submit" class="btn" name="led" value="off">
                    </form>
                </div>
            </body>
            </html>
        """

    def serve_forever(self):
        """Ejecuta el servidor web de forma continua"""
        try:
            # Iniciar el punto de acceso (AP)
            self.wifi.start_ap()
            
            # Configurar el servidor web
            if not self.wifi.setup_web_server():
                self.wifi.show_message("Error servidor")
                return
            
            # Bucle principal del servidor
            while True:
                conn = None
                try:
                    # Aceptar conexiones con timeout
                    conn, addr = self.wifi.server_socket.accept()
                    conn.settimeout(3.0)
                    
                    # Recibir la solicitud
                    request = conn.recv(1024).decode()
                    
                    # Acceder al valor del request para controlar el LED
                    if '/?led=on' in request:
                        print("LED ON")
                        led.value(1)
                    elif '/?led=off' in request:
                        print("LED OFF")
                        led.value(0)
                    
                    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                    conn.send(response.encode())
                    self.wifi.send_response(conn, self.web_html())
                    
                except Exception as e:
                    # Manejar errores de conexión
                    if 'ETIMEDOUT' not in str(e):
                        print(f"Error en conexión: {e}")
                finally:
                    if conn:
                        conn.close()
                
                sleep(0.1)
                
        except Exception as e:
            # Mostrar mensaje de error en caso de fallo
            self.wifi.show_message(f"E: {str(e)[:16]}")
            
def main():
    try:
        led.value(0)
        # Crear y ejecutar el servidor web
        server = CustomWebServer()
        server.serve_forever()
    except Exception as e:
        print(f"Error al iniciar el servidor: {e}")

if __name__ == "__main__":
    main()
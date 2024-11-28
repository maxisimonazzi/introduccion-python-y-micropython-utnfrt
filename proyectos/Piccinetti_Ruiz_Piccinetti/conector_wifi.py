from network import WLAN, STA_IF, AP_IF, AUTH_WPA2_PSK
import socket
from time import sleep, time
from machine import Pin, SoftI2C, unique_id
try:
    from ssd1306 import SSD1306_I2C
except ImportError as e:
    print(f"Error importing SSD1306: {e}")
import re
from json import dumps, loads
import select


class ConectorWIFI:
    def __init__(self, ap_ssid='WifiConector', ap_password='wificonector', debug=False):
        # Agregar verificación para el módulo WLAN
        if not hasattr(WLAN, 'active'):
            raise RuntimeError("WLAN module not properly initialized")
    
        # Inicialización OLED
        try:
            i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=1000000)
            # Agregar verificación para SoftI2C
            if not hasattr(i2c, 'readfrom'):
                raise RuntimeError("SoftI2C not properly initialized")
            self.oled = SSD1306_I2C(128, 64, i2c)
            self.display_ok = True
            self.show_message("Iniciando...")
            sleep(1)
        except Exception as e:
            print(f"Error iniciando OLED: {e}")
            self.display_ok = False

        self.wlan_sta = WLAN(STA_IF)
        self.wlan_ap = WLAN(AP_IF)
        self.wlan_sta.active(True)
        self.ap_ssid = ap_ssid
        self.ap_password = ap_password
        self.ap_authmode = AUTH_WPA2_PSK
        self.debug = debug
        self.connection_timeout = 15
        self.server_socket = None
        self.web_server_active = False
        self.last_display_update = time()
        self.display_page = 0

        self.ap_config = {
            'essid': self.ap_ssid,
            'password': self.ap_password,
            'authmode': self.ap_authmode,
            'channel': 11,
            'hidden': False,
            'max_clients': 10
        }

        self.wifi_credentials = 'wifi.dat.enc'
        self._salt = unique_id()
        self.max_failed_attempts = 5
        self.failed_attempts = {}

    def show_message(self, message, line=0, clear=True):
        """Muestra mensaje en consola y OLED"""
        print(message)
        if self.display_ok:
            try:
                # Solo limpiamos si clear=True y line=0
                if clear and line == 0:
                    self.oled.fill(0)
                # Limpiamos solo la línea específica si no es clear completo
                elif not clear:
                    # Limpia solo la línea específica (16 píxeles de alto por línea)
                    for y in range(line * 16, (line + 1) * 16):
                        for x in range(128):
                            self.oled.pixel(x, y, 0)
                
                # Divide el mensaje en líneas de máximo 16 caracteres
                words = message.split()
                lines = []
                current_line = ""
                for word in words:
                    if len(current_line + " " + word) > 16:
                        lines.append(current_line)
                        current_line = word
                    else:
                        current_line = (current_line + " " + word).strip()
                lines.append(current_line)
                
                # Muestra las líneas en el display
                for i, line_text in enumerate(lines[:1]):  # Solo mostramos una línea por llamada
                    self.oled.text(line_text, 0, line*16)
                self.oled.show()
            except Exception as e:
                print(f"Error en display: {e}")


    def update_status_display(self):
        """Actualiza el display con el estado actual"""
        self.oled.fill(0)
        
        # Primera línea: Estado AP
        if self.wlan_ap.active():
            self.oled.text(f"AP:{self.ap_ssid}", 0, 0)
            # Mostrar número de clientes conectados
            clients = len(self.wlan_ap.status('stations'))
            self.oled.text(f"Clients:{clients}", 0, 16)
        else:
            self.oled.text("AP:Inactivo", 0, 0)
        
        # Estado STA (si está conectado)
        if self.wlan_sta.isconnected():
            self.oled.text("WiFi:OK", 0, 32)
            ip = self.wlan_sta.ifconfig()[0]
            self.oled.text(ip, 0, 48)
        else:
            self.oled.text("WiFi:--", 0, 32)
        
        self.oled.show()
        self.last_display_update = time()

    def start_dual_mode(self):
        """Inicia el modo dual (AP + STA)"""
        self.show_message("Modo Dual", clear=True)
        sleep(1)
        
        try:
            # Iniciar el Access Point
            if not self.start_ap():
                self.show_message("Error AP", line=2)
                return False
            
            self.show_message("Iniciando STA...", line=2)
            connected = False
            profiles = self.read_credentials()
            
            # Intentar conectar a las redes guardadas
            for ssid, password in profiles.items():
                self.show_message(f"Prueba: {ssid}", line=3)
                if self.wifi_connect(ssid, password):
                    connected = True
                    break
            
            if not connected:
                self.show_message("Sin WiFi STA", line=3)
            
            # Configurar el servidor web
            if self.setup_web_server():
                self.web_server_active = True
                self.show_message("Modo Dual OK")
                if connected:
                    self.show_message(f"WiFi:{ssid}", line=1)
                    self.show_message(self.wlan_sta.ifconfig()[0], line=2)
                self.show_message(f"AP:{self.ap_ssid}", line=3)
                return True
            else:
                self.show_message("Error servidor")
                return False
                
        except Exception as e:
            self.show_message(f"Error: {str(e)[:16]}")
            return False

    def monitor_connections(self):
        """Monitorea el estado de las conexiones con actualización de display"""
        self.show_message("AP Activo", clear=True)
        self.show_message(f"SSID:{self.ap_ssid}", line=1)
        self.show_message("Esperando...", line=2)
        
        while True:
            try:
                # Actualizar display periódicamente
                current_time = time()
                if current_time - self.last_display_update >= 2:
                    self.update_status_display()
                
                # Verificar servidor web
                if not self.web_server_active:
                    self.setup_web_server()
                
                # Manejar conexión web
                if self.web_server_active and self.server_socket:
                    try:
                        # Usar select para manejar timeouts de manera más segura
                        ready_to_read, _, _ = select.select([self.server_socket], [], [], 0.1)
                        if ready_to_read:
                            self.handle_client_connection()
                    except OSError as e:
                        if e.args[0] not in [116, 128]:  # ETIMEDOUT, ENOTCONN
                            print(f"Error OSError: {e}")
                    except Exception as e:
                        print(f"Error en conexión web: {e}")
                
                # Verificar STA si está activo
                if self.wlan_sta.isconnected():
                    self.check_sta_connection()
                
                # Verificar AP
                if not self.wlan_ap.active():
                    self.show_message("Reiniciando AP...")
                    self.start_ap()
                
            except Exception as e:
                print(f"Error en monitor: {e}")
            
            sleep(0.1)

    
    def _encrypt_credentials(self, data):
        # Encripta las credenciales usando una clave basada en _salt
        encrypted = bytearray()
        key = self._salt
        for i, byte in enumerate(dumps(data).encode()):
            encrypted.append(byte ^ key[i % len(key)])
        return encrypted

    def _decrypt_credentials(self, encrypted_data):
        # Desencripta las credenciales usando una clave basada en _salt
        decrypted = bytearray()
        key = self._salt
        for i, byte in enumerate(encrypted_data):
            decrypted.append(byte ^ key[i % len(key)])
        try:
            return loads(decrypted.decode())
        except:
            return {}
        
    def connect(self):
        """Intento de conexión con credenciales guardadas; si falla, inicia AP"""
        self.show_message("Iniciando conexion", clear=True)
        sleep(1)
        
        if self.wlan_sta.isconnected():
            self.show_message("WiFi Conectado", line=1)
            self.show_message(self.wlan_sta.ifconfig()[0], line=2)
            return True

        self.show_message("Buscando redes...", line=2)
        profiles = self.read_credentials()
        sleep(1)
        for ssid, password in profiles.items():
            self.show_message(f"Intentando: {ssid}", line=2)
            if self.wifi_connect(ssid, password):
                self.show_message("Conexion OK!", line=3)
                sleep(1)
                return True

        self.show_message("Sin conexion", line=2)
        sleep(1)
        
        self.wlan_sta.disconnect()
        if not self.start_ap():
            self.show_message("Error AP", line=3)
            return False
            
        self.setup_web_server()
        
        while True:
            try:
                self.handle_client_connection()
            except Exception as e:
                self.show_message(f"Error: {str(e)[:16]}", line=3)
                sleep(1)

    def start_ap(self):
        """Inicia el Access Point para la configuración"""
        self.show_message("Iniciando AP...")
        self.wlan_ap.active(False)
        sleep(1)
        self.wlan_ap.active(True)
        
        try:
            self.wlan_ap.config(
                essid=self.ap_ssid,
                password=self.ap_password,
                authmode=self.ap_authmode,
                channel=11
            )
            
            if self.wlan_ap.active():
                self.show_message("AP:" + self.ap_ssid, line=1)
                self.show_message("PS:" + self.ap_password, line=2)
                self.show_message("IP:" + self.wlan_ap.ifconfig()[0], line=3)
                sleep(1)
                return self.wlan_ap.ifconfig()[0]
            
            self.show_message("Error AP", line=1)
            return False
            
        except Exception as e:
            self.show_message(f"Error: {str(e)[:16]}", line=1)
            return False

    def setup_web_server(self):
        """Configura el servidor web con mejor manejo de timeouts"""
        if self.server_socket:
            try:
                self.server_socket.close()
            except Exception:
                pass
            sleep(0.5)  # Dar tiempo para liberar el socket

        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.settimeout(0.1)  # Configurar timeout para el socket
            self.server_socket.bind(('', 80))
            self.server_socket.listen(1)
            self.web_server_active = True
            return True
        except Exception as e:
            print(f"Error en setup web server: {e}")
            self.web_server_active = False
            return False


    def check_sta_connection(self):
        """Verifica y maneja la conexión STA"""
        if not self.wlan_sta.isconnected():
            self.show_message("Reconectando...")
            profiles = self.read_credentials()
            for ssid, password in profiles.items():
                if self.wifi_connect(ssid, password):
                    break
                sleep(1)


    def handle_client_connection(self):
        """Manejo de conexión entrante en el servidor web"""
        try:
            conn, addr = self.server_socket.accept()
            conn.settimeout(3)
            request = conn.recv(1024).decode()
            
            # Extraer URL
            url = re.search('(?:GET|POST) /(.*?)(?:\\?.*?)? HTTP', request)
            if url:
                url = url.group(1).rstrip('/')
                if url == '':
                    self.handle_root(conn)
                elif url == 'configure':
                    self.handle_configure(conn, request, addr)
                else:
                    self.send_response(conn, "Página no encontrada", 404)
            conn.close()
        except socket.timeout:
            # Timeout normal, no hacer nada
            pass
        except OSError as e:
            # Manejar errores de socket específicamente
            if e.args[0] not in [116, 128]:  # ETIMEDOUT, ENOTCONN
                print(f"Error de socket: {e}")
        except Exception as e:
            if "ETIMEDOUT" not in str(e):
                print(f"Error en manejo de cliente: {e}")

    def handle_root(self, conn):
        """Genera y envía la página principal HTML para elegir WiFi"""
        networks = self.wlan_sta.scan()
        html_content = """
          <!DOCTYPE html>
            <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <style>
                        body { font-family: Arial, sans-serif; margin: 20px; }
                        .network-item { padding: 10px; margin: 5px 0; border: 1px solid #ddd; }
                        .signal-strength { float: right; }
                        .stats { margin: 20px 0; padding: 10px; background: #f5f5f5; }
                        .btn { padding: 5px;margin: 10px;font-size: 18px;cursor: pointer;border: none;border-radius: 5px;transition: background-color 0.3s;}
                    </style>
                    <title>Conector WIFI</title></head>
                <body>
                    <h2>Redes WiFi disponibles</h2>
                     
                    <form action="/configure" method="post">
                      
        """
        for ssid, bssid, channel, rssi, authmode, hidde in networks:
            ssid = ssid.decode('utf-8')
            signal_strength = min(100, max(0, int((rssi + 100) * 2)))
            # Agregar cada red WiFi encontrada al contenido HTML
            html_content += f'<div class="network-item"><input type="radio" name="ssid" value="{ssid}" id="{ssid}"><label for="{ssid}">{ssid}</label><span class="signal-strength">Signal: {signal_strength}%</span></div>'

        html_content += """
                        <p>Contraseña: <input type="password" name="password"></p>
                        <p><input type="submit" value="Conectar" class="btn"></p>
                    </form>
                    </body>
            </html>
        """
        self.send_response(conn, html_content)

    def handle_configure(self, conn, request, addr):
        """Manejo de la configuración con protección contra intentos fallidos"""
        client_ip = str(addr)
        if client_ip in self.failed_attempts and self.failed_attempts[client_ip] >= 5:
            self.send_response(conn, "Demasiados intentos fallidos. Intenta más tarde.", 403)     

        """Extrae y guarda las credenciales de la solicitud POST"""
        match_ssid = re.search(r'ssid=([^&]+)', request)
        match_password = re.search(r'password=([^&]*)', request)
        if match_ssid:
            ssid = match_ssid.group(1)
            password = match_password.group(1) if match_password else ""
            print(f"Recibido SSID: {ssid} y contraseña: {password}")
            if self.wifi_connect(ssid, password):
                # Guardar y probar conexión
                self.write_credentials({ssid: password})
                self.send_response(conn, "Conectado exitosamente.")
            else:
                # Si hay un fallo de autenticación:
                self.send_response(conn, "Error de conexión. Verifica tus credenciales.")
                self.failed_attempts[client_ip] = self.failed_attempts.get(client_ip, 0) + 1
        else:
            self.send_response(conn, "SSID no válido.", 400)
 
 

    def send_response(self, conn, content, status_code=200):
        """Envía una respuesta HTTP"""
        response = f"HTTP/1.1 {status_code} OK\r\nContent-Type: text/html\r\n\r\n{content}"
        conn.send(response.encode())

    def wifi_connect(self, ssid, password, max_retries=3):
        """Intento de conexión a WiFi con limitación de intentos"""
        # Limpiamos la pantalla al inicio
        self.show_message(f"SSID: {ssid}", line=0, clear=True)
        self.show_message(f"Conectando...", line=1, clear=False)
        
        for attempt in range(max_retries):
            self.show_message(f"Intento:{attempt+1}/{max_retries}", line=2, clear=False)
            
            self.wlan_sta.connect(ssid, password)
            start_time = time()
            
            while time() - start_time < self.connection_timeout:
                if self.wlan_sta.isconnected():
                    ip = self.wlan_sta.ifconfig()[0]
                    self.show_message("Conectado!", line=2, clear=False)
                    self.show_message(f"IP: {ip}", line=3, clear=False)
                    sleep(1)
                    return ip
                    
                # Actualizamos solo la línea de progreso
                self.show_message("." * int((time() - start_time)), line=3, clear=False)  # Padding fijo de 4
                sleep(0.5)

            self.wlan_sta.disconnect()
            self.show_message("Fallo conexion", line=3, clear=False)
            sleep(1)

        self.show_message("WiFi Error", line=3, clear=False)
        return False

    def read_credentials(self):
        """Lee credenciales guardadas desde el archivo JSON"""
        try:
            with open(self.wifi_credentials, 'rb') as file:
                encrypted = file.read()
            return self._decrypt_credentials(encrypted)
        except:
            return {}

    def write_credentials(self, profiles):
        """Guarda credenciales en un archivo JSON"""
        encrypted = self._encrypt_credentials(profiles)
        with open(self.wifi_credentials, 'wb') as file:
            file.write(encrypted)

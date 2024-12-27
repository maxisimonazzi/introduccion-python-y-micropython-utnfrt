# **🍽️ COMEDERO AUTOMÁTICO**

## 📄 Descripción
Este proyecto es un sistema de control para un comedero automático que utiliza un servo motor y una interfaz web para alimentarlo de forma remota. El sistema se conecta a una red Wi-Fi y expone una página web en la que se puede controlar el movimiento de un servo motor que activa el comedero.

## 🛠️ Componentes
- **ESP32**
- **Servo motor**
- **Red Wi-Fi** (para controlar el comedero de manera remota)

## 💻 Descripción del Código

### 🔧 Control de Servo Motor
El código utiliza la librería `machine` de MicroPython para controlar un servo motor conectado al pin GPIO 15. La función `mover_servo(angulo)` permite mover el servo a un ángulo específico dentro del rango de 0 a 180 grados.

### 🌐 Conexión Wi-Fi
Se establece una conexión Wi-Fi mediante la librería `network`. El dispositivo se conecta a la red especificada en las variables `ssid` y `password`.

### 🌍 Servidor Web
El código crea un servidor web que se ejecuta en el puerto 80 y proporciona una página HTML con un botón. Al presionar el botón, se envía una solicitud HTTP al servidor, lo que activa el movimiento del servo motor para alimentar al comedero.

### 🕹️ Control del Servo desde la Web
Al hacer clic en el botón de la página web, el servidor recibe la solicitud y mueve el servo a una posición de 50 grados durante 2 segundos antes de devolverlo a la posición de 140 grados, simulando el proceso de alimentar.

## ▶️ Ejecución
Una vez que el dispositivo esté configurado y conectado a la red Wi-Fi, abre un navegador web e ingresa la dirección IP del dispositivo (que se muestra en la salida del código en el terminal). La página web tendrá un botón que, al presionarlo, activará el comedero.

### Ejemplo de salida en el terminal:
```
Conectado a Wi-Fi
('192.168.1.10', '255.255.255.0', '192.168.1.1', '192.168.1.10')
Servidor en ejecución
Conexión desde ('192.168.1.20', 12345)
Solicitud: b'GET /mover HTTP/1.1 ...'
```

## 📷 Esquemático

![Esquemático del Comedero Automático](esquema.png)

El esquemático muestra la conexión del ESP32 con el servo motor y la red Wi-Fi. Asegúrate de seguir las conexiones correctamente para evitar daños en los componentes y asegurar el correcto funcionamiento del sistema.

## 🔗 **LINK SIMULACIÓN WOKWI**
[Simulación en Wokwi](https://wokwi.com/projects/416532584309852161)

## ⚠️ Consideraciones
- Asegúrate de que el servo motor esté conectado correctamente y no esté recibiendo más corriente de la que puede soportar.
- El sistema está diseñado para ser controlado desde cualquier navegador web conectado a la misma red Wi-Fi que el dispositivo.

## 🚀 Mejoras futuras
- Integrar control de velocidad del servo motor.
- Agregar autenticación para controlar el acceso al sistema.
- Añadir soporte para múltiples servidores o dispositivos.

## 👥 Participantes
- Mateo García
- Angel David Maná
- Gonzalo Suarez

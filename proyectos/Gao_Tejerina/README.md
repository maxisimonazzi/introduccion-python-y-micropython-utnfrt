# Proyecto del curso de Micropython
# Control Doble de LEDs RGB

Este proyecto permite controlar dos LEDs RGB conectados a una ESP32. Uno se maneja mediante una interfaz web y el otro con potenciómetros, 
mostrando los valores actuales en una pantalla LCD I2C. La conexión se realiza a través de la red Wi-Fi

---

## Características

1. **Control de LED RGB por Potenciómetros**:
   - Ajuste manual de los valores R (rojo), G (verde) y B (azul).
   - Visualización de los valores actuales en una pantalla LCD I2C.

2. **Control de LED RGB vía Web**:
   - Página web sencilla para enviar los valores RGB mediante el método GET.
   - Conexión a la ESP32 en la IP 10.0.0.15.

3. **Conectividad Wi-Fi**:
   - La ESP32 se conecta automáticamente a la red Wi-Fi especificada.
   - Configuración adicional de un Access Point (AP) con nombre Mi_ESP32_AP.

4. **Pagina de interfaz web**:
   - Pagina web con una interfaz sencilla de usar para controlar uno de los leds.
   - 3 espacios de edicion para los valores RGB y un botón para enviar la url con metodo GET.

---
## Componentes Utilizados

**Hardware**:

   - ESP32 con Wi-Fi.
   - 2 LEDs RGB de ánodo común.
   - 3 potenciómetros.
   - Pantalla LCD I2C.

**Software**:
   - MicroPython instalado en la ESP32.
   - Librerías: lcd_api.py e i2c_lcd.py.
   - Thonny
---
## Estructura del Proyecto

**Código Principal (MicroPython)**:
   - Conexión Wi-Fi.
   - Configuración de LEDs RGB y potenciómetros.
   - Configuración de la pantalla LCD I2C.
   - Servidor web para capturar parámetros RGB desde la interfaz.

**Código Web**:
   - HTML de estructura basica con anexo al css y al js.
   - Configuración del CSS para la estilo de la pagina.
   - Codigo JavaScript para manejar el cambio de color del background y envio de la url.


---

## Configuracón y Ejecución
1. Conexión de Hardware:
   - Conecta los LEDs RGB, los potenciómetros y la pantalla LCD a la ESP32.
2. Configuración Wi-Fi:
   - Configurar la red y la contraseña para la conexión Wi-Fi.
3. Cargar el Código:
   - Utiliza Thonny para cargar el script y las bibliotecas en la ESP32.
4. Pagina Web:
   - Abre y ejecuta el index.html.
   - Ajusta los valores RGB desde la página.

---

## Prueba del Circuito

Puedes ver una muestra de la ejecución del proyecto:  
**[Ver nuestra](https://www.youtube.com/watch?feature=shared&v=uVhq_q5yC8I)**

---

## Esquema del Circuito

A continuación se muestra el esquema de conexión del circuito:

![Esquema del Circuito](./esquema_de_conexion.jpeg)

---
## Experiencia y mejoras posibles

Como parte de la experiencia en el curso, este proyecto nos resultó muy útil. La parte más complicada fue la interacción entre la página web y la placa ESP32. 
Para superar las dificultades, recurrimos a la ayuda de internet y al apoyo de la IA en algunos casos.

En un primer momento, intentamos enviar los datos desde la ESP32 hacia la página web, pero no pudimos lograrlo. 
Optamos por enviar los datos desde la página a la placa, lo cual pudimos conseguir.

Aunque el control de los leds es visualmente llamativo, inicialmente no parece tener una aplicación práctica mas allá. Sin embargo, el verdadero objetivo 
del proyecto era aprender a enviar datos desde la web. Una vez que conseguimos este proceso, las posibilidades se ampliaron muchisimo. 
Ahora podemos controlar dispositivos como relés, motores paso a paso, servomotores, enviar mensajes a la pantalla LCD, entre otros.

Este proyecto, que en principio solo sirve para activar unos LEDs, tambien es una base sólida para desarrollar sistemas de control mucho más avanzados en el futuro.

---
## Muchas gracias por instruirnos profesor!!!
# Proyecto: MicroPython UTN-FRT - Trabajo Final

![MicroPython](https://img.shields.io/badge/MicroPython-v1.0-blue.svg)
![Python](https://img.shields.io/badge/Python-100%25-brightgreen.svg)

## Descripción

El archivo `main.py` es el núcleo del proyecto, encargado de conectar a una red WiFi, medir temperatura y humedad usando un sensor DHT22, y mostrar estos datos en una pantalla OLED.

## Implementación

El archivo está implementado en [MicroPython](https://micropython.org/), una implementación ligera de Python para microcontroladores. A continuación se describe la funcionalidad de cada componente del archivo `main.py`:

### Estructura del Código

- **Importaciones**:
    ```python
    import time
    from lib.net import conectar_wifi  
    from lib.net import obtener_hora_actual  
    from lib.sensor_dht22 import medir_temperatura, medir_humedad
    from lib.oled_display import mostrar_datos
    ```

- **Conexión a WiFi**:
    ```python
    conectar_wifi()
    ```

- **Bucle Principal**:
    ```python
    while True:
        temp = medir_temperatura()
        time.sleep(0.5) # Evita errores en la toma de mediciones
        hum = medir_humedad()
        
        time.sleep(1)
        datos_hora = obtener_hora_actual()

        if datos_hora is not None:
            print('Hora: {}'.format(datos_hora))
        if temp is not None:
            print('Temperatura: {}\u00b0C'.format(temp))
        if hum is not None:
            print('Humedad: {}%'.format(hum))
        mostrar_datos(temp, hum)

        # Esperar 2 segundos antes de la siguiente lectura
        time.sleep(2)
    ```

## Configuración

Para configurar el proyecto, sigue estos pasos:

1. Clonar el repositorio.
    ```bash
    git clone https://github.com/ceenov/micropython_utnfrt_tpfinal.git
    ```
2. Configurar los parámetros necesarios en los archivos de configuración dentro del directorio `lib`.

## Uso

Para ejecutar el archivo `main.py`, sigue estos pasos:

1. Conectar el microcontrolador a tu computadora.
2. Subir los archivos al microcontrolador
3. Reiniciar el microcontrolador para que ejecute el código.

## Dependencias

Este proyecto depende de las siguientes bibliotecas:

- [MicroPython](https://micropython.org/): Implementación de Python para microcontroladores.
- [Bibliotecas específicas del proyecto](https://github.com/ceenov/micropython_utnfrt_tpfinal/tree/main/lib): net, sensor_dht22, oled_display.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

[![UTN-FRT](https://img.shields.io/badge/UTN-FRT-blue.svg)](http://www.frt.utn.edu.ar/)
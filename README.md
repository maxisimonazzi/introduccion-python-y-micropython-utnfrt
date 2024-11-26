# 🐍 Curso Introducción a Python y Micropython 🐍
# UTN-FRT - Ingeniería Electrónica

Aqui encontrarás el material del curso **Introducción a Python y Micropython** dictado en la UTN-FRT por el instructor **Maximiliano Simonazzi**.

## 📄 Descripción

Este curso está diseñado para proporcionar una introducción completa a Python y Micropython, enfocándose en aplicaciones prácticas y control de hardware. A lo largo del curso, los estudiantes aprenderán los fundamentos de la programación en Python, así como su implementación en microcontroladores utilizando Micropython. El curso incluye tanto teoría como prácticas, permitiendo a los estudiantes aplicar los conceptos aprendidos en proyectos reales.

- **Duración:** 10 clases + 2 clases extra
- **Modalidad:** Presencial y a distancia
- **Requisitos:** Conocimientos básicos de programación (no excluyente)
- **Materiales:** Placa ESP32 Devkit v1, acceso a la plataforma Wokwi, protoboard, cables y componentes electrónicos básicos.

Este curso es ideal para aquellos que desean iniciarse en el mundo de la programación y el control de hardware, así como para quienes buscan ampliar sus conocimientos en estas áreas.

Durante el cursado se abordarán temas como la programación orientada a objetos, la comunicación serial y el control de hardware básico. Además, se realizarán prácticas en las que se aplicarán los conocimientos adquiridos en el curso.

Las practicas se realizarán de manera presencial con una placa ESP32 Devkit v1, y los que tomen el curso a distancia lo haran en la plataforma [Wokwi](https://wokwi.com/), una plataforma de simulación de hardware que permite simular con precisión el comportamiento del microcontrolador ESP32 con Micropython.

## 📚 Material del curso Introducción a Python y Micropython dictado en la UTN-FRT

### 📝 Índice de Clases

Todas las clases serán dictadas en el horario de 16:30 a 18:30.

<details>
<summary>Clase 1️⃣: 14 de Septiembre</summary>

Breve historia de Python y su Filosofía. Principios de diseño de Python (PEP 20). Instalación y Configuración de Python y entornos de desarrollo (IDE).

- **Diapositiva:** [Clase 1](Clase01.pdf)
- **Material Extra:**
  - [Python](https://www.python.org/)
  - [Visual Studio Code](https://code.visualstudio.com/)

</details>

<details>
<summary>Clase 2️⃣: 21 de Septiembre</summary>

Sintaxis Básica y Estructuras de Control. Variables, tipos de datos y operadores. Estructuras de control (if, for, while).

- **Diapositiva:** [Clase 2](Clase02.pdf)

</details>

<details>
<summary>Clase 3️⃣: 28 de Septiembre</summary>

Estructuras de Datos. Listas, tuplas, diccionarios y conjuntos. Manipulación y métodos asociados.

- **Diapositiva:** [Clase 3](Clase03.pdf)

</details>

<details>
<summary>Clase 4️⃣: 05 de Octubre</summary>

Funciones y Módulos. Definición y uso de funciones. Importación y creación de módulos.

- **Diapositiva:** [Clase 4](Clase04.pdf)

</details>

<details>
<summary>Clase 5️⃣: 12 de Octubre</summary>

Conceptos Básicos de POO. Clases y objetos. Métodos y atributos.

- **Diapositiva:** [Clase 5](Clase05.pdf)

</details>

<details>
<summary>Clase 6️⃣: 19 de Octubre</summary>

Qué es un microcontrolador y sus aplicaciones. Comparación entre MicroPython y otros lenguajes de programación para microcontroladores. Instalación de MicroPython en la placa ESP32. Introducción a la programación básica con MicroPython.

- **Diapositiva:** [Clase 6](Clase06.pdf)
- **Material Extra:**
  - [MicroPython](https://micropython.org/)
  - [Documentación de MicroPython](https://docs.micropython.org/en/latest/)
  - [Drivers CH9102X](https://www.wch-ic.com/downloads/CH343SER_ZIP.html)
  - [Drivers CH9102X en el repositorio](driverCH9102X/CH343SER.ZIP)
  - [Thonny](https://thonny.org/)
  - [Ejemplo en Wokwi: Blink con ESP32 y LED onboard](https://wokwi.com/projects/412197049127131137)

</details>

<details>
<summary>Clase 7️⃣: 26 de Octubre</summary>

Control de Hardware Básico. Manejo de pines GPIO. Lectura de sensores y actuadores.

- **Diapositiva:** [Clase 7](Clase07.pdf)
- **Ejemplos en Wokwi:**
  - [Uso de tres LEDs](https://wokwi.com/projects/412813092810329089)
  - [Tres LEDs y tres botones](https://wokwi.com/projects/412816619189701633)
  - [Potenciómetro](https://wokwi.com/projects/412823150331085825)
  - [PWM con un LED](https://wokwi.com/projects/412827239122614273)
  - [Manejo de un servo con potenciómetro](https://wokwi.com/projects/412828987952574465)
  - [Módulo DHT22](https://wokwi.com/projects/412832035326576641)
  - [Gráfica PWM en Desmos](https://www.desmos.com/calculator/wsspteh4rc?lang=es)

</details>

<details>
<summary>Clase 8️⃣: 09 de Noviembre</summary>

Comunicación Serial. UART, I2C, SPI. Comunicación entre dispositivos.

- **Diapositiva:** [Clase 8](Clase08.pdf)
- **Ejemplos en Wokwi:**
  - [Escáner de bus I2C](https://wokwi.com/projects/414079834163793921)
  - [Display LCD 2x16 con I2C](https://wokwi.com/projects/414082182853706753)
  - [Display LCD 2x16 con caracteres custom](https://wokwi.com/projects/414082835855619073)
  - [Display LCD 2x16 con sensor de temperatura](https://wokwi.com/projects/414083765618679809)
  - [Dos displays LCD 2x16 con sensor de temperatura](https://wokwi.com/projects/414085167768395777)
  - [Display OLED SSD1306](https://wokwi.com/projects/414092239396279297)
  - [Display OLED SSD1306 con sensor de temperatura](https://wokwi.com/projects/414092844302002177)
  - [Creador de caracteres para LCD](https://maxpromer.github.io/LCD-Character-Creator/)

</details>

<details>
<summary>Clase 9️⃣: 16 de Noviembre</summary>

Estación. Punto de acceso. Web server.

- **Diapositiva:** [Clase 9](Clase09.pdf)

</details>

<details>
<summary>Clase 1️⃣0️⃣: 23 de Noviembre</summary>

Laboratorio: Control de LEDs, botones y buzzer mediante pulsadores y por internet.

- **Ejemplos en Wokwi:**
  - [LEDs, botones y buzzer](https://wokwi.com/projects/414134246575354881)
  - [Juego Simon](https://wokwi.com/projects/414937512735548417)
  - [Notificación por Whatsapp](https://wokwi.com/projects/415309631171881985)

</details>

<details>
<summary>Clase Extra 1️⃣: 8 de Octubre</summary>

Bibliotecas Estándar y Externas. Introducción a las bibliotecas estándar de Python. Uso de bibliotecas populares (NumPy, matplotlib).

- **Diapositiva:** [Clase Extra 1](Clase_extra01.pdf)

</details>

<details>
<summary>Clase Extra 2️⃣: 29 de Octubre</summary>

Trabajando en equipo. Git y GitHub.

- **Diapositiva:** [Clase Extra 2](Clase_extra02.pdf)

</details>
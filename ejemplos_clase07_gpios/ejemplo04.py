from machine import Pin, ADC
from time import sleep

# Configurar los pines de los leds como salidas
led_verde = Pin(15, Pin.OUT)
led_amarillo = Pin(4, Pin.OUT)
led_rojo = Pin(5, Pin.OUT)

# Configurar el pin ADC (GPIO 34)
adc_pin = ADC(Pin(13))

# Configurar el ancho de bits de la lectura ADC (opcional, por defecto es 12 bits)
# Podemos configurar una resolucion de 9 a 12 bits (512, 1024, 2048 y 4096 valores).
adc_pin.width(ADC.WIDTH_12BIT)

# Configurar la atenuación (opcional, por defecto es 11dB)
# Podemos configurar la atenuación en 0dB, 2.5dB, 6dB, 11dB.
# La atenuación ATTN_0DB en 0dB permite medir entre 0V y 1.1V
# La atenuación ATTN_2_5DB en 2.5dB permite medir entre 0V y 1.5V
# La atenuación ATTN_6DB en 6dB permite medir entre 0V y 2.2V
# La atenuación ATTN_11DB en 11dB permite medir entre 0V y 3.3V
adc_pin.atten(ADC.ATTN_11DB)

# Definir la resolución del ADC y el voltaje de referencia
resolucion_adc = 4095  # Para 12 bits
tension_referencia = 3.3  # Voltaje de referencia en voltios

while True:
    # Leer el valor ADC
    adc_valor = adc_pin.read()
    
    # Convertir el valor ADC a voltios
    tension = (adc_valor / resolucion_adc) * tension_referencia
    
    # Imprimir el valor ADC y el voltaje
    print('Valor ADC:', adc_valor, '- Tension:', tension, 'V')

    if 0 <= adc_valor <= 500:
        led_amarillo.off()
        led_rojo.off()
        led_verde.off()
    if 500 < adc_valor <= 2000:
        led_amarillo.off()
        led_rojo.off()
        led_verde.on()
    if 2000 < adc_valor <= 3000:
        led_amarillo.on()
        led_rojo.off()
        led_verde.on()
    if 3000 < adc_valor <= 4095:
        led_amarillo.on()
        led_rojo.on()
        led_verde.on()

    
    # Esperar un momento antes de la siguiente lectura
    sleep(0.5)
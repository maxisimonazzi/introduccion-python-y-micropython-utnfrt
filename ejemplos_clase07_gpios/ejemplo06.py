from machine import Pin, ADC, PWM
import utime

servo =PWM(Pin(19))
servo.freq(50)
adc = ADC(Pin(13))

while True:
    potenciometro = int(adc.read()*180/4095) # valor en grados
    ton=(potenciometro+45)*100000/9
    servo.duty_ns(int(ton))
    print('Valor ADC:', adc.read(), "- Tiempo de ON:", ton/1000000,"ms")
    utime.sleep_ms(50)
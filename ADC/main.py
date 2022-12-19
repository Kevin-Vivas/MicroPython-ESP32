import time
from machine import Pin, PWM,ADC

adc1 =ADC(Pin(4))
pwm32 = PWM(Pin(18))
pwm32.freq(1000)
#pwm32.duty(512)

def Principal():
    while True:
        print("El valor en micro voltios es {}".format(adc1.read_uv()))
        print("El valor numerico es {}".format(adc1.read()))
        print("CODIGO")
        valor = (adc1.read_uv()/1042)
        print(valor)
        pwm32.duty(int(valor))  
        time.sleep_ms(250)
"""
def PWM():
    pwm32 = PWM(Pin(18))
    pwm32.freq(1000)    
    pwm32.duty(adc1.read())
    print(pwm32)
    pwm32.duty_u16(8257)
    
    """   

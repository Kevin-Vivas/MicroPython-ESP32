import time
from machine import Pin, PWM, ADC

mensaje = "hdkdf12345"
pwm32 = PWM(Pin(5))
pwm32.freq(5000)
pwm32.duty(int(mensaje))

"""
def Principal():
    while True:
        pwm32 = PWM(Pin(5))
        pwm32.freq(1000)
        pwm32.duty(1023)

"""
        



    







"""
import time
from machine import Pin, PWM, ADC

def Principal():
    while True:
        
        print("Control del led")
        valor = float(input("Ingrese el valor"))*1023/100
        print("eL  valor es:",str(valor))
        print("Resultado",str(valor))
        time.sleep(2)
        pwm32 = PWM(Pin(18))
        pwm32.freq(1500)
        pwm32.duty(int(valor))
        print(pwm32)
        


        




'''
import time
from machine import Pin, PWM

pwm32 = PWM(Pin(18))
pwm32.freq(1000)
pwm32.duty(512)

def Principal():
    pwm32 = PWM(Pin(18))
    pwm32.freq(1000)    
    pwm32.duty(512)
    print(pwm32)
    pwm32.duty_u16(8257)

    
"""

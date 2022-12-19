# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, PWM
from time import sleep

def Principal():
    while True:

        pwm32 = PWM(Pin(5))
        pwm32.freq(5000)
        pwm32.duty(512)
        print(pwm32)
    




"""
import time
from machine import Pin, PWM, ADC

pwm32 = PWM(Pin(32))
pwm32.freq(1500)
pwm32.duty(512)
print(pwm32)










import time
from machine import Pin, PWM, ADC

def Principal():
    while True:
        
        print("Control del led")
        valor = float(input("Ingrese el valor"))*1023/100
        print("eL  valor es:",str(valor))
        print("Resultado",str(valor))
        
        pwm32 = PWM(Pin(4))
        pwm32.freq(1500)
        pwm32.duty(int(valor))
        print(pwm32)
        time.sleep(4)

        
        

        

        

        
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


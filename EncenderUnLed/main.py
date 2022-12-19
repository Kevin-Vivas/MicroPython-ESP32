import time
from machine import Pin, PWM


def Principal():
    gpio4 = Pin(4,Pin.OUT)

    while True:
        print("Encender pin 4")
        gpio4.on()  #value puede ser verdadero o falso
        time.sleep_ms(125)
        print("Apagar pin 4")
        gpio4.off()
        time.sleep_ms(125)                

print(" \n\n...............Inicio Programa..................\n\n")

#gpio4 = Pin(4,Pin.OUT)
#gpio16 = Pin(16,Pin.IN ) #(Pin number, pin mode, pull, value)
print(" \n\n...............Termino Programa..................\n\n")


   

#Kevin





#gpio4 = Pin(4,Pin.OUT)
#gpio16 = Pin(16,Pin.OUT)

"""
while True:
    print("Encender pin 4")
    gpio4.on()
    time.sleep_ms(1000)
    print("pin off 16")
    gpio16.off()
    time.sleep(1)
    print("Apagar pin 16")
    gpio4.off()
    time.sleep_ms(1000)
    gpio16.on()
    print("Pin on ")
    time.sleep(1)
    """

    

    




#for i in range(10):
    #print("El programa termina en {} segundos".format(10-i))
    #time.sleep(1)
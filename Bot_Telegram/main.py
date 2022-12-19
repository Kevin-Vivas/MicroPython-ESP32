import wlan
import Telegram
from machine import Pin
import time
from umqtt.simple import MQTTClien


wlan.do_connect()

ledrojo=(4,Pin.OUT)
ledazul=(2,Pin.OUT)

def Led1On(topico,mensaje):
    print(mensaje)
    if(mensaje == b'LED ROJO'):
        ledrojo.on()
        ledazul.off()


cliente = MQTTClient(' Prende_Tu_Primer_Led_bot/cliente1','RASPBERRY_IP')
cliente.set_callback(encender)
cliente.connect()
cliente.subscribe(b"Prende_Tu_Primer_Led_bot/ejemplo1")

while True:
    cliente.check_msg()
    time.sleep_ms(100)

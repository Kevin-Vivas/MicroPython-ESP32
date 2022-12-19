# DHT11 JESUS 
from machine import Pin
from time import sleep
import dht 

#sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(4))

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')





"""

# DHT11 JESUS 
from machine import Pin
from time import sleep
import dht 

#sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(4))

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')



#DHT11 KEVIN
import time
from  machine import Pin,PWM , ADC , I2C
import dht

sensor = dht.DHT11(machine.Pin(4))
sensor.measure()
temp = sensor.temperature()
hum = sensor.humidity()
text = "Temp:{}  Hum:{} ".format(temp,hum)


def  Principal():
    while True:
        time.sleep_ms(2000)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        text = "Temp:{}  Hum:{} ".format(temp,hum)
        print(text)




#Ejemplo
while True:
    dht.measure()
    dht.temperature() #eg. 23 (°C)
    dht.humidity()    #eg. 41 (% RH)
    print("Temp:{}°C" , "Hum: {} %RH".format(str(dht.temperature()),str(dht.humidity())))
    time.sleep_ms(1000)
"""

import time
from machine import Pin, PWM, ADC, I2C
import ssd1306
#import ssd1306
import dht

print("\n\n -------------------------- Inicio del programa --------------------------\n\n")

i2c = I2C(0, scl=Pin(18), sda=Pin(19), freq=400000)

display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hola Mundo', 0, 0, 1)
display.show()

def Principal():
    while True:
        pass

print("\n\n -------------------------- Termino el programa --------------------------\n\n")



'''
from machine import Pin, SoftI2C , PWM,ADC
from time import sleep
import time
import ssd1306


# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World 1!', 0 , 0, 1)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
oled.text('SENSOR TEMP!', 0, 30)




oled.invert (True)
#oled.invert (False)
        
oled.show()
'''
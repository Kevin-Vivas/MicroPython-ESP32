import time, network, dht, uping, utelegram, ssd1306

from machine import Pin, PWM, ADC, I2C

renglon1 = {"x": 0, "y": 0}
renglon2 = {"x":0, "y": 8}
renglon3 = {"x":0, "y": 16}
renglon4 = {"x":0, "y": 24}
renglon5 = {"x":0, "y": 32}
renglon6 = {"x":0, "y": 40}
renglon7 = {"x":0, "y": 48}
renglon8 = {"x":0, "y": 56}
highLine = 8
widthLine = 127
timeoutLimit = 60000


ssid = "ECCI-Estudiantes"
password = "Estudiantes2021."
#ssid = "T PEREZ"
#password = "tp10052781"
telegramToken = "5825356274:AAGZccUJmYaKV8cdyLE5bGaPiVNMjaCRHw4"
#ssid = "T PEREZ"
#password = "tp10052781"
#telegramToken = "5880832499:AAEXnXwfNX3Na57V5e4d_M2Mil-I5uQsxYk" 
#ssid = "ECCI-Estudiantes"
#telegramToken = "5880832499:AAEXnXwfNX3Na57V5e4d_M2Mil-I5uQsxYk"


print("\n\n -------------------------- Inicio del programa --------------------------\n\n")

def get_message(message):
    value = message['message']['text']
    value1= message['message']['text']
    #numero = re.split('[^0-9]*', "{}".format(value), flags=re.IGNORECASE)
    
    
    
    print(type(value))

 
    
    print(value)
    display.fill_rect(renglon3["x"], renglon3["y"], widthLine, highLine, 0)
    display.show()
    display.text(value1,renglon2["x"], renglon2["y"], 1)
    display.show()
    

    if value=="Led" :
        print(" Selecion Led ")
        bot.send(message['message']['chat']['id'], "5 profe")
        bot.send(message['message']['chat']['id'], "5 profe")
        #bot.send(message['message']['chat']['id'], "Aquí ponen lo que quieren enviar a telegram")
        




                        

        

        
def reply_ping(message):
    

    time.sleep(2)
    sensor = dht.DHT11(Pin(4))
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)

    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    display.fill_rect(renglon3["x"], renglon3["y"], widthLine, highLine, 0)
    display.show()
    display.fill_rect(renglon4["x"], renglon4["y"], widthLine, highLine, 0)
    display.show()   
    display.text("Temperatura:{}C".format(temp),renglon2["x"], renglon2["y"], 1)
    display.show()
    display.text("Temperatura:{}F".format(temp_f),renglon3["x"], renglon3["y"], 1)
    display.show()
    display.text("Humedad:{}RH".format(hum),renglon4["x"], renglon4["y"], 1)
    display.show()
    bot.send(message['message']['chat']['id'],"Temperatura:{} C  Temperatura:{}F , Humedad:{}RH".format(temp,temp_f,hum))
    
    time.sleep(10)
    display.fill_rect(renglon4["x"], renglon4["y"], widthLine, highLine, 0)
    display.show()
    display.fill_rect(renglon3["x"], renglon3["y"], widthLine, highLine, 0)
    display.show()
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    
    pass                                     
    #bot.send(message['message']['chat']['id'], 'pong')
  
def Led100(message):

    mensaje="EL LED SE PERENDIO AL 100%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((100)*(1023))/100
    display.text("LED: {}% ".format(str(100)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass

def Led90(message):
    numero= 90
    mensaje="EL LED SE PERENDIO AL 90%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((numero)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass

def Led80(message):
    numero= 80
    mensaje="EL LED SE PERENDIO AL 80%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((numero)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass

def Led70(message):
    numero= 70
    mensaje="EL LED SE PERENDIO AL 70%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((numero)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass
    
def Led60(message):
    numero= 60
    mensaje="EL LED SE PERENDIO AL 60%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((numero)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass    

def Led50(message):
    numero= 50
    mensaje="EL LED SE PERENDIO AL 50%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((numero)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass 

def Led40(message):
    numero= 40
    mensaje="EL LED SE PERENDIO AL 40%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((numero)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass 

def Led30(message):
    numero= 30
    mensaje="EL LED SE PERENDIO AL 30%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((30)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass 

def Led20(message):
    numero= 20
    mensaje="EL LED SE PERENDIO AL 30%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((20)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass 

def Led10(message):
    numero= 10
    mensaje="EL LED SE PERENDIO AL 10%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((numero)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass 

def Led10(message):
    numero= 10
    mensaje="EL LED SE PERENDIO AL 10%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((numero)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass 

def Led0(message):
    numero= 0
    mensaje="EL LED ESTA APAGADO%"
    bot.send(message['message']['chat']['id'],"{}".format(mensaje))
    duty = ((numero)*(1023))/100
    display.text("LED: {}% ".format(str(numero)),renglon2["x"], renglon2["y"], 1)
    display.show()
    pwm32 = PWM(Pin(5))
    pwm32.freq(1000)
    pwm32.duty(int(duty))
    time.sleep(4)
    display.fill_rect(renglon2["x"], renglon2["y"], widthLine, highLine, 0)
    display.show()
    pass 




    
     




def Principal():

    print("The bot is listening")
    display.text("bot is listening", renglon5["x"], renglon5["y"], 1)
    display.show()
    bot.listen()

i2c = I2C(0, scl=Pin(18), sda=Pin(19), freq=400000)
#display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.show()
display.text("MicroPython ECCI", renglon1["x"], renglon1["y"], 1)
display.show()

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)

print("Connecting to WiFi ...")
wlan.connect(ssid, password)
start_time = time.ticks_ms()
while not wlan.isconnected():
    if time.ticks_diff(time.ticks_ms(), start_time) > timeoutLimit:
        print("No se pudo establecer la conexción a WiFi, se superó el límite de tiempo")
        break
print("Connected")
uping.ping("google.com")

if wlan.isconnected():
    print("Creating telegram bot")
    bot = utelegram.ubot(telegramToken)
    bot.set_default_handler(get_message)
    bot.register('Temperatura', reply_ping)
    bot.register('100', Led100)
    bot.register('90', Led90)
    bot.register('80', Led80)
    bot.register('70', Led70)
    bot.register('60', Led60)
    bot.register('50', Led50)
    bot.register('40', Led40)
    bot.register('30', Led30)
    bot.register('20', Led20)
    bot.register('10', Led10)
    bot.register('apagar', Led0)
    
    print("The Telegram bot was created")
    display.text("Bot was created", renglon6["x"], renglon6["y"], 1)
    display.show()


    



print("\n\n -------------------------- Termino el programa --------------------------\n\n")
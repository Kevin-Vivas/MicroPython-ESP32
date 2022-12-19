import time, network,ssd1306, uping, utelegram 
from machine import Pin, PWM, ADC, I2C

ssid = "T PEREZ"
password = "tp10052781"
telegramToken = "5880832499:AAEXnXwfNX3Na57V5e4d_M2Mil-I5uQsxYk" # Ojo aqui va el token de su BOT no del mio 

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)

def Connect2Wifi():
    print("Connecting to WiFi ...")
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print("Connected")
    uping.ping("google.com")

def get_message(message):
    value = message['message']['text']
    print(value)
    #bot.send(message['message']['chat']['id'], message['message']['text'].upper())

def reply_ping(message):
    print(message)
    #bot.send(message['message']['chat']['id'], 'pong')

def Principal():
    Connect2Wifi()

    if wlan.isconnected():
        print("Creating telegram bot")
        bot = utelegram.ubot(telegramToken)
        bot.register('/ping', reply_ping)
        bot.set_default_handler(get_message)
        print("The Telegram bot was created")
    
    print("The bot is listening")
    bot.listen()

print("\n\n -------------------------- Inicio del programa --------------------------\n\n")
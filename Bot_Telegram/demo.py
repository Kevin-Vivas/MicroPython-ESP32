import paho.mqtt.client as mqtt
import time

def on_connect(client,userdata,flags,rc):
    print("Conectado")

Client =mqtt.Client()
Client.on_connect=on_connect
Client.connect()

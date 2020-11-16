import paho.mqtt.client as mqtt
import time
import logging

logging.basicConfig(filename="client1log.txt", level=logging.DEBUG)
def on_connect(client,userdata,flags,rc): #connection request
    print("Connected - rc:",rc)
def on_message(client,userdata,message):#when client receives msg on subscribed topic
    global FLAG
    global chat
    try:
        if str(message.topic) != pubtop:
            msg = str(message.payload.decode("utf-8"))
            print(str(message.topic),msg)
            logging.debug(message.topic),msg  # external file logging in debug level
            logging.debug(msg)
            if msg == "Stop" or msg == "stop":
                FLAG = False #to disconnect 
            elif msg == "1":
                    print("cannot chat with 1 alone")
                    FLAG = False
            else:
                    chat = input("Enter Message: ")
                    client.publish(pubtop,chat)
    except Exception as e:
        logging.debug(e)
def on_subscribe(client, userdata,mid,granted_qos):# subscribe request.
    print("Subscribed:", str(mid),str(granted_qos))
def on_unsubscirbe(client,userdata,mid):#unsubscribed request.
    print("Unsubscribed:",str(mid))
def on_disconnect(client,userdata,rc):# disconnects from the broker
    if rc !=0:
        print("Unexpected Disconnection")


broker_address = "mqtt.eclipse.org"
port = 1883

client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscirbe
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address,port)

time.sleep(1)

pubtop = "/chat/client1"
subtop = "/chat/client2"
FLAG = True

client.loop_start()
client.subscribe(subtop)

time.sleep(1)
chat = input("Enter Message: ")
client.publish(pubtop,chat)
while True:
    if FLAG == False or chat == "Stop" or chat == "stop":
        break

client.disconnect()
client.loop_stop()

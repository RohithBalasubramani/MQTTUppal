import paho.mqtt.client as mqtt

# MQTT broker details
broker = "broker.hivemq.com"
port = 1883
client_id = "asdas"  # Ensure this is unique for your client
username = "admin"  # Public broker usually doesn't need this
password = "admin"  # Public broker usually doesn't need this

# Topics
publish_topic = "SNEAPLuppalP"
response_topic = "SNEAPLuppalR"
subscribe_topic = "SNEAPLuppalS"
birth_topic = "Start"
last_will_topic = "End"


# Callback for connection
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to topics
    client.subscribe(publish_topic)
    client.subscribe(response_topic)
    client.subscribe(subscribe_topic)
    client.subscribe(birth_topic)
    client.subscribe(last_will_topic)

# Callback for receiving messages
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

# Setup MQTT client with callback API version 5
client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

# Optional: Set username and password for the broker if required
# client.username_pw_set(username, password)

# Connect to the broker
client.connect(broker, port, 60)

# Start the loop to process callbacks and handle reconnections
client.loop_forever()

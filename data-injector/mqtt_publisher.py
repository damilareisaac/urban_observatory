from paho.mqtt import client as mqtt_client
import json
import time


class MqttPublisher:
    def __init__(self, host="localhost"):
        # server variables
        self.mqtt_port = 1883
        self.mqtt_host = host
        self.mqtt_topic = "CSC8112"

        # Create a mqtt client object
        self.client = mqtt_client.Client()

        # Connect to MQTT service
        self.client.on_connect = self.on_connect

        self.client.connect(self.mqtt_host, self.mqtt_port)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"MQTT Edge Server  Connected!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def publish(self, msg=None):
        msg = json.dumps(msg)
        print(f"Message {msg} Published from MQTT EDGE")
        self.client.publish(self.mqtt_topic, msg)

from paho.mqtt import client as mqtt_client
import json
from queue import Queue


class MqttSubscriber:
    def __init__(self, host="localhost", topic="CSC8112"):
        # server variables
        self.mqtt_port = 1883
        self.mqtt_host = host
        self.mqtt_topic = topic

        # initailize msg as None
        self.message_queue = Queue()
        # Create a mqtt client object
        self.client = mqtt_client.Client()

        # Connect to MQTT service
        self.client.on_connect = self.on_connect
        self.client.connect(self.mqtt_host, self.mqtt_port)

        self.subscribe()

        self.client.on_message = self.on_message

        self.client.loop_start()

    def on_connect(self, client=None, userdata=None, flags=None, rc=None):
        if rc == 0:
            print(f"MQTT CLOUD Server subscriber connected!", flush=True)
        else:
            print(f"Failed to connect, return code {rc}", flush=True)

    def on_message(self, client, userdata, msg):
        message = json.loads(msg.payload.decode("utf8"))
        # print(f"{message} FROM MQTT publisher", flush=True)
        self.message_queue.put(message)

    def subscribe(self, topic=None):
        # Subscribe MQTT topic
        if not topic:
            topic = self.mqtt_topic
        print(f"Subscribe to topic: {topic}", flush=True)
        # Start a thread to monitor message from publisher
        self.client.subscribe(topic)

    @property
    def message_from_queue(self):
        print("returning message queue")
        return self.message_queue

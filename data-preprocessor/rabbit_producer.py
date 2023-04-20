import pika
import json


class RabbitProducer:
    def __init__(self, host="localhost"):
        self.rabbitmq_host = host
        self.rabbitmq_port = 5672
        self.rabbitmq_username = "guest"
        self.rabbitmq_password = "guest"
        # Queue name
        self.rabbit_vhost = "/"

        # credentials
        self.credentials = pika.PlainCredentials(
            self.rabbitmq_username, self.rabbitmq_password
        )

        # parameters
        self.parameters = pika.ConnectionParameters(
            self.rabbitmq_host, self.rabbitmq_port, self.rabbit_vhost, self.credentials
        )

        self.connection = pika.BlockingConnection(self.parameters)

        # create a channel to receive
        self.channel = self.connection.channel()

        # Declare a queue
        self.channel.queue_declare(queue=self.rabbit_vhost)

    def publish(self, message="Hello"):
        # Produce message
        print(message)
        message = json.dumps(message)
        self.channel.basic_publish(
            exchange="", routing_key=self.rabbit_vhost, body=message
        )
        print(
            f"RABBIT BROKER publishing {message} to queue '{self.rabbit_vhost}'",
            flush=True,
        )

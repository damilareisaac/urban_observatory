from time import time
import pika
import json
from queue import Queue


class RabbitConsumer():
    def __init__(self, host='localhost'):
        self.__rabbitmq_host = host
        self.__rabbitmq_port = 5672
        self.__rabbitmq_username = "guest"
        self.__rabbitmq_password = "guest"
        # Queue name
        self.__rabbit_vhost = "/"

        #message_queue
        self.__message_queue = Queue()

        # credentials
        self.__credentials = pika.PlainCredentials(
            self.__rabbitmq_username,
            self.__rabbitmq_password)

        # parameters
        self.__parameters = pika.ConnectionParameters(
            self.__rabbitmq_host,
            self.__rabbitmq_port,
            self.__rabbit_vhost,
            self.__credentials)

        self.__connection = pika.BlockingConnection(self.__parameters)

        # create a channel to receive
        self.__channel = self.__connection.channel()

        # Declare a queue
        self.__channel.queue_declare(queue=self.__rabbit_vhost)

        self.__channel.basic_consume(queue=self.__rabbit_vhost,
                                     auto_ack=True,
                                     on_message_callback=self.__callback)

        print('Started Consuming')
        self.__channel.start_consuming()

        

    def __callback(self, ch, method, properties, body):
        body = json.loads(body)
        print(f'Type of message body {type(body)}', flush=True)
        self.__message_queue.put(body)
        self.__channel.stop_consuming()
        # print(f"{self.__message_queue.get(block=False, timeout=2)} FROM RABBIT QUEUE", flush=True)

    @property
    def message_queue(self):
        print('This was called')
        return self.__message_queue

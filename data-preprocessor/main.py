from mqtt_subscriber import MqttSubscriber
from preprocessor import DataPreprocessor
from rabbit_producer import RabbitProducer


while True:
    mqtt_subscriber = MqttSubscriber('localhost')

    message = mqtt_subscriber.message_from_queue.get()

    # print(f'message is {message.get()}.', flush=True)
    data_preprocessor = DataPreprocessor(message)
    

    average_by_days = data_preprocessor.average_by_days

    rabbit_queue = RabbitProducer('192.168.0.100')

    rabbit_queue.publish(average_by_days)

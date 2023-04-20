from mqtt_publisher import MqttPublisher
from injector import DataInjector
import time


while True:
    data_injector = DataInjector()
    request_data = data_injector.time_series_data
    mqtt_pub = MqttPublisher()
    mqtt_pub.publish(request_data)
    time.sleep(4)
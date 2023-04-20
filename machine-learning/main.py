from rabbit_consumer import RabbitConsumer
import pandas as pd
from datetime import datetime

rabbit_consumer = RabbitConsumer()
message = rabbit_consumer.message_queue.get()
# print(f'{message} FROM EDGE RABBIT PRODUCER', flush=True)

message_df = pd.DataFrame(message)

DATE_FORMAT  = '%Y-%m-%d %H:%M:%S'

message_df['Timestamp'] = message_df['Timestamp'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d').strftime(DATE_FORMAT))
print(message_df)

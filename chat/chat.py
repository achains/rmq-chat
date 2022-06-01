import os
import sys
from datetime import datetime
import uuid

import pika

from chat.consumer import Consumer
from chat.publisher import Publisher

__all__ = ["Chat"]


class Chat:
    def __init__(
        self,
        nickname,
        host="localhost",
        port=5672,
        topic="flood",
        exchange_name="mainfs",
    ):
        self.connection_params = pika.ConnectionParameters(host=host, port=5672)
        self.nickname = nickname
        self.host = host
        self.port = port
        self.topic = topic
        self.topic_queues = {topic: self.__create_new_queue_name()}
        self.consumer = Consumer(
            queue_name=self.get_current_queue(),
            topic=topic,
            connection_params=self.connection_params,
        )
        self.publisher = Publisher(
            exchange_name=exchange_name, connection_params=self.connection_params
        )
        self.exchange_name = exchange_name

    def get_current_queue(self):
        return self.topic_queues[self.topic]

    def change_topic(self, new_topic):
        self.consumer.stop_consuming()
        self.topic = new_topic
        if new_topic not in self.topic_queues:
            self.topic_queues[new_topic] = self.__create_new_queue_name()
        self.consumer = Consumer(
            queue_name=self.get_current_queue(),
            topic=self.topic,
            connection_params=self.connection_params,
        )
        self.consumer.start_consuming()

    def send_message(self, msg: str):
        self.publisher.publish(self.__create_message(msg), self.topic)

    def activate(self):
        self.consumer.start_consuming()

    def finish(self):
        print("== Closing connection ==")
        self.consumer.stop_consuming()

    def __create_message(self, base_msg):
        time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        return f"{self.nickname} [{time}]: {base_msg}"

    def __create_new_queue_name(self):
        return uuid.uuid4().hex

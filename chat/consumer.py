import threading

import pika

__all__ = ["Consumer"]


class Consumer:
    def __init__(
        self,
        queue_name,
        topic,
        connection_params: pika.ConnectionParameters,
        exchange_name="mainfs",
    ):
        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.topic = topic
        self.channel.exchange_declare(
            exchange=self.exchange_name, exchange_type="direct"
        )
        self.message_queue = self.channel.queue_declare(queue=self.queue_name)
        self.channel.queue_bind(
            exchange=self.exchange_name,
            queue=self.message_queue.method.queue,
            routing_key=topic,
        )

        self.channel.basic_consume(
            queue=self.message_queue.method.queue,
            on_message_callback=lambda ch, method, properties, body: print(
                body.decode()
            ),
            auto_ack=True,
        )

        self.consumer_thread: threading.Thread = threading.Thread(
            target=self.channel.start_consuming
        )

    def start_consuming(self):
        print(f"[INFO] Current topic {self.topic}")
        self.consumer_thread.start()

    def stop_consuming(self):
        self.connection.add_callback_threadsafe(lambda: self.channel.stop_consuming())
        self.consumer_thread.join()

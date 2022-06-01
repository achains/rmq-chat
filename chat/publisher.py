import pika

__all__ = ["Publisher"]


class Publisher:
    def __init__(self, exchange_name, connection_params: pika.ConnectionParameters):
        self.exchange_name = exchange_name
        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()
        self.channel.exchange_declare(
            exchange=self.exchange_name, exchange_type="direct"
        )

    def publish(self, text: str, topic):
        self.channel.basic_publish(
            exchange=self.exchange_name, routing_key=topic, body=text.encode()
        )

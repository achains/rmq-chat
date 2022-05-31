#!/usr/bin/env python
import os
import sys
import threading
from datetime import datetime

import pika


class Command:
    def __init__(self):
        pass

    def execute(self):
        pass


def start_consuming():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs_new', exchange_type='direct')
    result = channel.queue_declare(queue='', exclusive=True)

    topic = sys.argv[1]

    queue_name = result.method.queue

    channel.queue_bind(exchange='logs_new', queue=queue_name, routing_key=topic)

    def callback(ch, method, properties, body):
        print(body.decode())

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs_new', exchange_type='direct')

    my_thread = threading.Thread(target=start_consuming)
    my_thread.start()

    while True:
        text = input('')
        now = datetime.now()
        time = now.strftime("%m/%d/%Y, %H:%M:%S")
        text = f"[{time}]: " + text
        channel.basic_publish(exchange='logs_new', routing_key=sys.argv[1], body=text)

    connection.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

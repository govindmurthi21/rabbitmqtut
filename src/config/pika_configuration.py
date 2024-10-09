import pika

def init_default_connection():
    connection_params = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_params)
    return connection.channel(), connection

def declare_default_queue(channel: pika.adapters.blocking_connection.BlockingChannel, queue_name: str):
    channel.queue_declare(queue=queue_name)

def close_connection(connection: pika.BlockingConnection):
    if connection.is_open:
        connection.close()

from src.config.pika_configuration import init_default_connection, declare_default_queue, close_connection

def produce(message: str):
    channel, connection = init_default_connection()
    declare_default_queue(channel, 'firstQueue')
    channel.basic_publish(exchange='', routing_key='firstQueue', body=message)
    close_connection(connection)
    





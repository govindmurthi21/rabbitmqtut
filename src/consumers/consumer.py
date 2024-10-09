from src.config.pika_configuration import init_default_connection, declare_default_queue, close_connection, basic_consume

def on_message_received(ch, method, props, body):
    print(f'The message has been received: {body}')

def run():
    channel, connection = init_default_connection()
    declare_default_queue(channel, 'firstQueue')
    basic_consume(channel, 'firstQueue', on_message_received)
    print('Start Consuming')
    channel.start_consuming()
    
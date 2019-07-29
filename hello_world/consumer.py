import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()


def callback(channel, method, properties, body):
    print('[X] Receive {body}'.format(body=body))

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print('[*] Waiting for message to exit press C+Strg')
channel.start_consuming()


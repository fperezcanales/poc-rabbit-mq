import pika, os

url = os.environ.get('CLOUDAMQP_URL')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a chanel
channel.queue_declare(queue='test_queue') # declare queue

def callback(ch, method, properties, body):
    print(' Recived ' + str(body))

channel.basic_consume(
    'test_queue',
    callback,
    auto_ack=True
)

print(' Waiting for messages:')
channel.start_consuming()
connection.close()
import pika, os

url = os.environ.get('CLOUDAMQP_URL')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a chanel

channel.exchange_declare('test_exchange') # declare exchange
channel.queue_declare(queue='test_queue') # declare queue
channel.queue_bind('test_queue', 'test_exchange', 'tests') # create binding between queue and exchange

channel.basic_publish(
    body='Tercer mensaje from fernando publisher',
    exchange='test_exchange',
    routing_key='tests'
)

print(' message sent')
channel.close()
connection.close()
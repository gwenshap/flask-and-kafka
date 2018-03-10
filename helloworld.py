from flask import Flask
from kafka import KafkaProducer
import logging
import json

def get_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=['r0.kafka-mt-1.us-west-2.aws.stag.cpdev.cloud:9092',
                           'r0.kafka-mt-1.us-west-2.aws.stag.cpdev.cloud:9093',
                           'r0.kafka-mt-1.us-west-2.aws.stag.cpdev.cloud:9094'],
        value_serializer=lambda m: json.dumps(m).encode('ascii'),
        retry_backoff_ms=500,
        request_timeout_ms=20000,
        security_protocol='SASL_SSL',
        sasl_mechanism='PLAIN',
        sasl_plain_username='OEPJVGM5NEHVWRV4',
        sasl_plain_password='y2u15Gou/nxzp72tyyt8d0O+7ztWJipZQySUiKWuzY0qSNes2KmH/dqvunY4zj0s')

# print a nice greeting.
def say_hello(username = "World"):
    # record the event asynchronously
    producer.send('webapp', {'says-hello' : username})
    return '<p>Hello %s!</p>\n' % username


logging.basicConfig(level=logging.DEBUG)

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Create a Kafka Producer
producer=get_kafka_producer()

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

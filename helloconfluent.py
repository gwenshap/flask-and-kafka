from flask import Flask
from confluent_kafka import Producer
import logging
import json

def get_kafka_producer():
    return Producer({'sasl.mechanisms':'PLAIN',
                     'request.timeout.ms': 20000,
                     'bootstrap.servers':'SASL_SSL://r0.kafka-mt-1.us-west-2.aws.stag.cpdev.cloud:9092,r0.kafka-mt-1.us-west-2.aws.stag.cpdev.cloud:9093,r0.kafka-mt-1.us-west-2.aws.stag.cpdev.cloud:9094',
                     'retry.backoff.ms':500,
                     'sasl.username':'OEPJVGM5NEHVWRV4',
                     'sasl.password':'y2u15Gou/nxzp72tyyt8d0O+7ztWJipZQySUiKWuzY0qSNes2KmH/dqvunY4zj0s',
                     'security.protocol':'SASL_SSL'})

# print a nice greeting.
def say_hello(username = "World"):
    # record the event asynchronously
    producer.produce('webapp', username + ', says-hello')
    return '<p>Hello %s!</p>\n' % username


logging.basicConfig(level=logging.DEBUG)

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>Flask and Kafka</title> </head>\n<body>'''
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

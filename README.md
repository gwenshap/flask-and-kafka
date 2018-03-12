# Flask, Kafka-Python and Confluent Cloud Example

Small example of how to create a webapp that produces events to Confluent Cloud.

## Instructions

* You will need a Confluent Cloud account. Make sure you have a list of bootstrap servers, API key and API secret. Contact Confluent to get those: https://www.confluent.io/cloud-contact/

* Since this is a small and shitty example, you'll need to edit the code and put in your own bootstrap servers, API Key (aka "username") and API Secret (aka "password").

* Create a virtual python environment: `virtualenv ~/venv/flask`

* Activate it: `source ~/venv/flask/bin/activate`

* Install required dependencies: `pip install -r requirements.txt`

* You'll also need to create your test topic (Confluent Cloud doesn't seem to support auto-create): `ccloud topic create webapp`

* You should have gotten ccloud CLI with your Cloud account, but just in case: https://github.com/confluentinc/examples/tree/master/ccloud

* To run an example that uses kafka-python client: `FLASK_APP=helloworld.py flask run`

* To run an example that uses confluent-kafka client: `FLASK_APP=helloconfluent.py flask run`

* If you get any weird connectivity errors, most likely you have issues with bootstrap servers, API keys or API secrets. Timeouts are usually because you didn't create the topic.

* Weird errors with confluent-kafka client may be related to the version. When in doubt, make sure you on 0.11.4rc1 or higher: `pip uninstall confluent_kafka` followed by `pip install --pre --index-url https://test.pypi.org/simple/ confluent_kafka`

* You can check that the app works with the ccloud consumer: `consume -b -t webapp`

from flask import Flask, jsonify, request
from google.protobuf.json_format import Parse
import requests
import json
import policy_pb2;
import argparse
from uuid import uuid4
from confluent_kafka import Producer
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer

app = Flask(__name__)

global health
health = "Unknown"

@app.route("/health", methods=["POST"])
def healthupdate():
    global health
    healthmessage=[{'healthstatus':health}]
    return(jsonify(healthmessage))

@app.route("/policyupdate", methods=["POST"])
def policyupdate():
    processedcomplete = [{'processed':"complete"}]
    processedfailed = [{'processed':"fail"}]
    processingstatus=processedcomplete
    global health
    health="Unknown"
    policy_json_request=request.get_json()
    print("Creating policy protobuf message")

    my_policy = Parse(json.dumps(policy_json_request),
      policy_pb2.Policy())

    try:
      producer.produce(topic=args.topic, key=str(uuid4()), value=my_policy)
      producer.flush()
    except confluent_kafka.KafkaError as e:
      print("Kafka Error: %s" % e)
      processingstatus=processedfailed
      health="endpoint policyupdate had a backend call http error to " + str(e)
    else:
      print("######################## Good")
      health="Good"

    return( jsonify(processingstatus) )

def main():
    global args
    parser=argparse.ArgumentParser()
    parser.add_argument("topic", help="'TOPIC'")
    parser.add_argument("reg", help="'reg'")
    parser.add_argument("broker", help="'broker'")
    args = parser.parse_args()

    # Setup Producer
    schema_registry_conf = {'url': args.reg} #input arg
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    protobuf_serializer = ProtobufSerializer(policy_pb2.Policy,
                                             schema_registry_client)
    #input arg bootstrap.servers
    producer_conf = {'bootstrap.servers': args.broker,
                       'key.serializer': StringSerializer('utf_8'),
                       'value.serializer': protobuf_serializer}
    global producer
    #librdkafka library which contains the c implementation of SerializingProducer does not through exceptions. Only log messages will be available.
    producer = SerializingProducer(producer_conf)


    app.run(host='0.0.0.0', port=8000)

if __name__ == "__main__":
    main()

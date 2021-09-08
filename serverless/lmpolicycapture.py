#!/usr/bin/env python3

# Processes a POST json request and sends an http CloudEvent to Kafka
#

from flask import Flask, jsonify, request
import requests
import json
import policy_pb2;
import argparse
from uuid import uuid4
from google.protobuf.json_format import Parse
from confluent_kafka import Producer
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer

app = Flask(__name__)

global processingstatus
global health
health = "Unknown"

@app.route("/health", methods=["POST"])
def healthupdate():
    global health
    healthmessage=[{'healthstatus':health}]
    return(jsonify(healthmessage))

@app.route("/policyupdate", methods=["POST"])
def policy_update():
    global processingstatus
    processedincomplete = [{'processed':"incomplete"}]
    processedcomplete = [{'processed':"complete"}]
    processedfailed = [{'processed':"fail"}]
    processingstatus=processedincomplete
    global health
    health="Unknown"

    policy_json_request=request.get_json()
    print("Creating policy protobuf message")

    my_policy = Parse(json.dumps(policy_json_request),
      policy_pb2.Policy())

    schema_registry_conf = {'url': "http://schemaregistry-0.schemaregistry.confluent.svc.cluster.local:8081"}
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    protobuf_serializer = ProtobufSerializer(policy_pb2.Policy,
                                             schema_registry_client)

    #input arg bootstrap.servers
    producer_conf = {'bootstrap.servers': "PLAINTEXT://kafka.confluent.svc.cluster.local:9071",
                     'key.serializer': StringSerializer('utf_8'),
                     'value.serializer': protobuf_serializer}

    producer = SerializingProducer(producer_conf)
    try:
      producer.produce(topic="policy-protobuf", key=str(uuid4()), value=my_policy)
      producer.flush()
      processingstatus=processedcomplete
    except:
      print ("Error: Producer")
      processingstatus=processedfailed
      health="endpoint policyupdate had a backend call error to topic"

    return(jsonify(processingstatus) )

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    main()

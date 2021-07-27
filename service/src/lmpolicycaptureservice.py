#!/usr/bin/env python3

# Processes a POST json request and sends an http CloudEvent to Kafka
#
# ex: curl -XPOST -H "Content-Type: application/json" --data '{"policyNumber": 400, "policyPrice": 3500.75, "policyDetails": "Auto Policy with three cars"}' http://127.0.0.1:8000/policyupdate
#

import io
import requests
import json
import policy_pb2
import argparse
from uuid import uuid4
from flask import Flask, jsonify, request
from cloudevents.http import CloudEvent, to_binary, from_http
from google.protobuf.json_format import Parse
from confluent_kafka import Producer
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer

app = Flask(__name__)
status = [{'status':"processed"}]

@app.route("/policyupdate", methods=["POST"])
def get_name():



policy = event.data.read();

# create a CloudEvent
    event = from_http(
        request.headers,
        request.get_data(),
        data_unmarshaller=lambda x: io.BytesIO(x),
    )

    policy = event.data.read();

    ds = policy_pb2.Policy();
    ds.ParseFromString(policy);
    print("Dserializing")
    print(ds);

    # create a CloudEvent
    event = from_http(
        request.headers,
        request.get_data(),
        data_unmarshaller=lambda x: io.BytesIO(x),
    )
    ds = policy_pb2.Policy();
    ds.ParseFromString(policy);
    print("Dserializing")
    print(ds);

    topic = 'pb-test'  #input arg
    #schema_registry_conf = {'url': args.schema_registry}
    schema_registry_conf = {'url': 'http://localhost:8081'} #input arg
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    protobuf_serializer = ProtobufSerializer(policy_pb2.Policy,
                                             schema_registry_client)

    #input arg bootstrap.servers
    producer_conf = {'bootstrap.servers': 'localhost:9092',
                     'key.serializer': StringSerializer('utf_8'),
                     'value.serializer': protobuf_serializer}

    producer = SerializingProducer(producer_conf)
    producer.produce(topic=topic, key=str(uuid4()), value=ds)
    producer.flush()

    return jsonify(status)

def main():
    #app.run(host='0.0.0.0', port=8000)
    app.run(port=8080)

if __name__ == "__main__":
    main()
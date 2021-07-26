from flask import Flask, jsonify, request
from cloudevents.http import CloudEvent, to_binary
import requests
import json
from confluent_kafka import Producer

app = Flask(__name__)


status = [{'status':"processed"}]

@app.route("/policyupdate", methods=["POST"])
def get_name():
    policy_json_request=request.get_json()

    attributes = {
        "type": "policy",
        "source": "https://policy.lmig.com/event-producer",
    }
    event = CloudEvent(attributes, policy_json_request)
    print("CloudEvent: ")
    print(event)
    producer = Producer(bootstrap_servers='ipofkafka:9092')
    producer.send('policytopicname', str(event).encode())
    return jsonify(status)

def main():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()

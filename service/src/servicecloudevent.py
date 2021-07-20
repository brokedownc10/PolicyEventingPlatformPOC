from flask import Flask, jsonify, request
from cloudevents.http import CloudEvent, to_binary
from google.protobuf.json_format import Parse
import requests
import json
import Policy_pb2
app = Flask(__name__)


accounts = [{'status':"processed"}]

@app.route("/policyupdate", methods=["POST"])
def get_name():
    policy_json_request=request.get_json()
    print("Creating policy protobuf message")

    message = Parse(json.dumps({
        "policyNumber": 100,
        "policyPrice": 2000.75,
        "policyDetails": "Auto Policy with two cars"
    }), Policy())

    attributes = {
        "type": "policy",
        "source": "https://policy.lmig.com/event-producer",
    }
    event = CloudEvent(attributes, policy_json_request)
    print("CloudEvent:")
    print(event)

    return jsonify(accounts)

def main():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()

from flask import Flask, jsonify, request
from cloudevents.http import CloudEvent, to_binary
from google.protobuf.json_format import Parse
import requests
import json
import Policy_pb3_pb2


app = Flask(__name__)


status = [{'status':"processed"}]

@app.route("/policyupdate", methods=["POST"])
def get_name():
    policy_json_request=request.get_json()
    print("Creating policy protobuf message")

    message = Parse(json.dumps(policy_json_request),
      Policy_pb3_pb2.Policy())

    attributes = {
        "type": "policy",
        "source": "https://policy.lmig.com/event-producer",
    }
    event = CloudEvent(attributes, message)
    print("CloudEvent:" + event)

    return jsonify(status)

def main():
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()

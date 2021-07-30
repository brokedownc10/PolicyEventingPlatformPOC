from flask import Flask, jsonify, request
from google.protobuf.json_format import Parse
import requests
import json
import policy_pb2;
from cloudevents.http import CloudEvent, to_binary
import argparse

app = Flask(__name__)

status = [{'status':"processed"}]


@app.route("/policyupdate", methods=["POST"])
def policyupdate():
    policy_json_request=request.get_json()
    print("Creating policy protobuf message")

    my_policy = Parse(json.dumps(policy_json_request),
      policy_pb2.Policy())
    send_binary_cloud_event(my_policy)

def send_binary_cloud_event(my_policy):
    print(args.url)
    # Create cloudevent
    attributes = {
        "type": "com.example.string",
        "source": "https://example.com/event-producer",
    }

    # Create a policy protobuf
    #my_policy = policy_pb2.Policy();
    #my_policy.policyNumber  = 100;
    #my_policy.policyPrice   = 2000;
    #my_policy.policyDetails = "Auto and Home Insurance";
    pb_data = my_policy.SerializeToString()
    event = CloudEvent(attributes, pb_data)

    # Create cloudevent HTTP headers and content
    headers, body = to_binary(event)

    # Send cloudevent
    requests.post(args.url, headers=headers, data=body)
    #print(f"Sent {event['id']} of type {event['type']}")

if __name__ == "__main__":
    # expects a url from command line.
    # e.g. python3 client.py http://localhost:3000/
    global args
    parser=argparse.ArgumentParser()
    parser.add_argument("url", help="'url'")
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=8080)

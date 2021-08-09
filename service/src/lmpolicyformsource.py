from flask import Flask, jsonify, request
from google.protobuf.json_format import Parse
import requests
import json
import policy_pb2;
from cloudevents.http import CloudEvent, to_binary
import argparse

app = Flask(__name__)

processedcomplete = [{'processed':"complete"}]
processedfailed = [{'processed':"fail"}]

global health
health = "Unknown"

@app.route("/health", methods=["POST"])
def healthupdate():
    global health
    healthmessage=[{'healthstatus':health}]
    return(jsonify(healthmessage))

@app.route("/policyupdate", methods=["POST"])
def policyupdate():
    policy_json_request=request.get_json()
    print("Creating policy protobuf message")

    my_policy = Parse(json.dumps(policy_json_request),
      policy_pb2.Policy())
    return(send_binary_cloud_event(my_policy))

def send_binary_cloud_event(my_policy):
    processingstatus=processedcomplete
    global health
    health="Good"
    print(args.url)
    # Create cloudevent
    attributes = {
        "type": "com.example.string",
        "source": "https://example.com/event-producer",
    }

    # Create a policy protobuf
    pb_data = my_policy.SerializeToString()
    event = CloudEvent(attributes, pb_data)

    # Create cloudevent HTTP headers and content
    headers, body = to_binary(event)

    # Send cloudevent
    try:
      response=requests.post(args.url, headers=headers, data=body)
    except requests.exceptions.HTTPError as errh:
      print ("Http Error:",errh)
      processingstatus=processedfailed
      health="endpoint policyupdate had a backend call http error to " + str(errh)
    except requests.exceptions.ConnectionError as errc:
      print ("Error Connecting:",errc)
      processingstatus=processedfailed
      health="endpoint policyupdate had a backend call error connecting to " + str(errc)
    except requests.exceptions.Timeout as errt:
      processingstatus=processedfailed
      print ("Timeout Error:",errt)
      health="endpoint policyupdate had a backend call timeout error to " + str(errt)
    except requests.exceptions.RequestException as err:
      print ("Error: Something Else",err)
      processingstatus=processedfailed
      health="endpoint policyupdate had a backend call error to " + str(err)

    return(jsonify(processingstatus) )

if __name__ == "__main__":
    # expects a url from command line.
    # e.g. python3 client.py http://localhost:3000/
    global args
    parser=argparse.ArgumentParser()
    parser.add_argument("url", help="'url'")
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=8000)

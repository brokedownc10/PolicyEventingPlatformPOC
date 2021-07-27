import io
import sys
import requests
import json
import policy_pb2;
import base64
from cloudevents.http import CloudEvent, to_binary

def send_binary_cloud_event(url: str):
    # Create cloudevent
    attributes = {
        "type": "com.example.string",
        "source": "https://example.com/event-producer",
    }

    # Create a policy protobuf
    my_policy = policy_pb2.Policy();
    my_policy.policyNumber  = 100;
    my_policy.policyPrice   = 2000;
    my_policy.policyDetails = "Auto and Home Insurance";
    pb_data = my_policy.SerializeToString()

    event = CloudEvent(attributes, pb_data)
    # Create cloudevent HTTP headers and content
    headers, body = to_binary(event)
    # Send cloudevent
    requests.post(url, headers=headers, data=body)
    print(f"Sent {event['id']} of type {event['type']}")

if __name__ == "__main__":
    # expects a url from command line.
    # e.g. python3 client.py http://localhost:3000/
    if len(sys.argv) < 2:
        sys.exit(
            "Usage: python with_requests.py " "<CloudEvents controller URL>"
        )

    url = sys.argv[1]
    send_binary_cloud_event(url)


##Docker way

#docker build . -t service
#https://www.docker.com/blog/containerized-python-development-part-1/
#docker run -d -p 5000:5000 --ip 172.17.0.9 service

#https://stackoverflow.com/questions/41614837/run-a-docker-with-specific-ip-address

docker network create --subnet=172.18.0.0/16 network_name


You first need to create a network:

docker network create --subnet=172.18.0.0/16 network_name

Then, when running a container, you can specify an IP address for it with the flags:

--net network_name --ip 172.18.0.XX

https://medium.com/swlh/how-to-run-locally-built-docker-images-in-kubernetes-b28fbc32cc1d


## More of a Kube way

start docker engine

minikube start
minikube dashboard

ps -elf | grep docker  (look for the process port)

minikube docker-env          
export DOCKER_TLS_VERIFY=”1"
export DOCKER_HOST=”tcp://127.0.0.1:<port number>"
export DOCKER_CERT_PATH=”/home/user/.minikube/certs”
export MINIKUBE_ACTIVE_DOCKERD=”minikube”

eval $(minikube -p minikube docker-env)

docker build . -t service

docker images <- list out the images

kubectl apply -f service.yml

kubectl cluster-info

kubectl apply -f namespace.yml


message policy  {int32 policyNumber = 1;  double policyPrice = 2;  string policyDetails = 3;}


### Protobuf creation ######################################

python3 version -> 3.8

Based on https://developers.google.com/protocol-buffers/docs/pythontutorial
What I think needs to be done is:

Install proto3 on Mac

  brew install protobuf

Break out the protobuf definition from the .py file. Put it in a file named: Policy.proto  Compile policy.proto using protoc so you are left with policy__pb3_pb2.py

from the service directory run

##>> protoc -I=./src --python_out=src src/Policy.proto

In the python file, import policy_pb3
Then you can change line 22 to: message = Parse(json.dumps({…}),policy_pb3.Policy())


## Knative integration

## https://knative.dev/docs/eventing/samples/helloworld/helloworld-python/

## Kafka integration

## https://timber.io/blog/hello-world-in-kafka-using-python/


## Building Docker image

##  docker build . -t <docker hub account name>/<imagename>:<version>

##  docker push <docker hub account name>/<imagename>:<version>

## Google Cloud Platform

## gcloud init
## gcloud auth login

## gcloud container clusters list

## gcloud container clusters get-credentials <cluster>

## kubectl apply -f ./<service.yml>

## kubectl get pods
## kubectl get svc
## kubectl get ingress

## kubectl exec -it <pod> -- /bin/bash

## kubectl get ksvc


# research
https://github.com/edenhill/librdkafka/blob/master/INTRODUCTION.md#ssl
https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/_modules/confluent_kafka/serializing_producer.html


## curl -X POST -H "Content-Type: application/json" --data '{"policyNumber": 400, "policyPrice": 3500.75, "policyDetails": "Auto Policy with three cars"}' http://lmpolicycapture-knative.default.35.238.210.88.sslip.io/policyupdate

##Kafka

## kubectl exec -it connect-0 -n confluent -- /usr/bin/kafka-topics --zookeeper zookeeper:2181/kafka-confluent --topic   policy-protobuf --replication-factor 3 --partitions 4 --create

## kubectl exec -it connect-0 -n confluent -- /usr/bin/kafka-topics --zookeeper zookeeper:2181/kafka-confluent --list | grep -v confluent

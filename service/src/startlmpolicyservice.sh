#!/usr/bin/env bash
# Script: run service
#########################################################
## Process paramters

exit_with_usage()
{
   echo "Usage: startlmpolicyservice.sh -s <SERVICE> -h <HOST> -p <PORT> -u <URL> -t <TOPIC>"
   echo "--"
   echo "Usage: ./startlmpolicyservice.sh -s lmpolicyformsource -h 127.0.0.1 -p 8080 -u 'http://127.0.0.1:8081'"
   echo "--"
   echo "Usage: ./startlmpolicycaptureservice.sh -s lmpolicyformsource -h 127.0.0.1 -p 8080 -b 'PLAINTEXT://kafka.confluent.svc.cluster.local:9071' -t my-topic -r 'http://schemaregistry-0.schemaregistry.confluent.svc.cluster.local:8081'"
   exit 1
}

#########################################################
## Process parameters
## List of options the program will accept;
## those options that take arguments are followed by a colon
optstring="s:h:p:u:t:b:"

## The loop calls getopts until there are no more options on the command line
## Each option is stored in $opt, any option arguments are stored in OPTARG
while getopts $optstring opt;
do
  case $opt in
    s) SERVICE=$OPTARG ;;
    h) HOST=$OPTARG ;;
    p) PORT=$OPTARG ;;
    u) URL=$OPTARG ;;
    b) BROKER=$OPTARG ;;
    r) REG=$OPTARG ;;
    t) TOPIC=$OPTARG ;;
   \?) exit_with_usage ;;
  esac
done

echo "$SERVICE"
echo "$HOST"
echo "$PORT"
echo "$URL"
echo "$BROKER"
echo "$REG"
echo "$TOPIC"

#if [ -z "$SERVICE" ]
#then
#  exit_with_usage
#  exit
#fi

#if [ -z "$HOST" ]
#then
#  exit_with_usage
#  exit
#fi

#if [ -z "$PORT" ]
#then
#  exit_with_usage
#  exit
#fi

#if [ -z "$URL" ]
#then
#  exit_with_usage
#  exit
#fi

if [ "$SERVICE" == 'lmpolicyformsource' ]; then
   python ./lmpolicyformsource.py $HOST $PORT $URL
else
   python ./lmpolicycaptureservice.py $HOST $PORT $TOPIC $REG $BROKER
fi

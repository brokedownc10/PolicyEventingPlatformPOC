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
   echo "Usage: ./startlmpolicycaptureservice.sh -s lmpolicyformsource -h 127.0.0.1 -p 8080 -u 'http://127.0.0.1:8081' -t my-topic"
   exit 1
}

#########################################################
## Process parameters
## List of options the program will accept;
## those options that take arguments are followed by a colon
optstring="s:h:p:u:t:"

## The loop calls getopts until there are no more options on the command line
## Each option is stored in $opt, any option arguments are stored in OPTARG
while getopts $optstring opt;
do
  case $opt in
    s) SERVICE=$OPTARG ;;
    h) HOST=$OPTARG ;;
    p) PORT=$OPTARG ;;
    u) URL=$OPTARG ;;
    t) TOPIC=$OPTARG ;;
   \?) exit_with_usage ;;
  esac
done

echo "$SERVICE"
echo "$HOST"
echo "$PORT"
echo "$URL"
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
   python ./lmpolicyformsource.py $HOST:$PORT:$URL
else
   python ./lmpolicycaptureservice.py $HOST:$PORT:$URL:$TOPIC
fi

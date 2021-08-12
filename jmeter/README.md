kubectl get pod -l serving.knative.dev/service=knative-example215 -w

kubectl exec -it loadgenerator -- /bin/bash

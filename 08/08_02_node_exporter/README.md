# Commands

    kubectl apply -f deployment.yaml

        deployment.apps/node-exporter created

    kubectl get deployments.apps node-exporter

        NAME            READY   UP-TO-DATE   AVAILABLE   AGE
        node-exporter   1/1     1            1           28s

    kubectl get pods

        NAME                             READY   STATUS    RESTARTS   AGE
        node-exporter-5ddbdb4548-k92gl   1/1     Running   0          50s

    kubectl describe deployments.apps node-exporter  | grep Port

        Port:       9100/TCP

    kubectl port-forward deployment/node-exporter 9100:9100

        Forwarding from 127.0.0.1:9100 -> 9100
        Forwarding from [::1]:9100 -> 9100

    kubectl delete -f deployment.yaml

        deployment.apps "node-exporter" deleted

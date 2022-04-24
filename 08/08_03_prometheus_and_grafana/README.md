# Commands

    kubectl apply -f manifests/

        configmap/prometheus-config created
        deployment.apps/grafana created
        deployment.apps/node-exporter created
        deployment.apps/prometheus created
        service/prometheus created

    kubectl get services

        NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
        prometheus      ClusterIP   10.107.118.116   <none>        9090/TCP   2m9s

    kubectl get deployments.apps

        NAME            READY   UP-TO-DATE   AVAILABLE   AGE
        grafana         1/1     1            1           2m5s
        node-exporter   1/1     1            1           2m5s
        prometheus      1/1     1            1           2m5s

    kubectl describe deployments.apps grafana  | grep Port

        Port:       3000/TCP

    kubectl port-forward deployment/grafana 3000:3000

        Forwarding from 127.0.0.1:3000 -> 3000
        Forwarding from [::1]:3000 -> 3000
        Handling connection for 3000

    kubectl delete -f manifests/

        configmap "prometheus-config" deleted
        deployment.apps "grafana" deleted
        deployment.apps "node-exporter" deleted
        deployment.apps "prometheus" deleted
        service "prometheus" deleted

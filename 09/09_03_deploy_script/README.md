    kubectl apply -f manifests/namespace.yaml

        namespace/tensor created

    kubectl apply -f manifests/

        configmap/configmap-env created 
        deployment.apps/my-app created
        namespace/tensor unchanged
        secret/mysql-secret configured
        service/mysql created 
        statefulset.apps/mysql created

    kubectl get deploy -n tensor

        NAME         READY   UP-TO-DATE   AVAILABLE   AGE
        my-app   1/1     1            1               3m59s

    kubectl port-forward deployment/my-app 8000:80 -n tensor

        Forwarding from 127.0.0.1:8000 -> 80
        Forwarding from [::1]:8000 -> 80
        Handling connection for 8000

    kubectl delete -f manifests/

        configmap "configmap-env" deleted
        deployment.apps "my-app" deleted
        namespace "tensor" deleted
        secret "mysql-secret" deleted
        service "mysql" deleted
        statefulset.apps "mysql" deleted

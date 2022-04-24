# Commands

    eval $(minikube docker-env)
    docker build -t python-app app/

        Sending build context to Docker daemon   5.12kB
        Step 1/8 : FROM python:3.10
        ---> 2b7ca628da40
        Step 2/8 : RUN mkdir -p /app
        ---> Using cache
        ---> ba2f958be0ad
        Step 3/8 : WORKDIR /app
        ---> Using cache
        ---> 7c5ca2bdb957
        Step 4/8 : COPY requirements.txt requirements.txt
        ---> Using cache
        ---> 16df2364504e
        Step 5/8 : RUN pip install --no-cache-dir -r requirements.txt
        ---> Using cache
        ---> 402b592579d1
        Step 6/8 : COPY . .
        ---> Using cache
        ---> 9910d776422b
        Step 7/8 : EXPOSE 9080
        ---> Using cache
        ---> 122e3054463d
        Step 8/8 : CMD ["python", "exporter.py"]
        ---> Using cache
        ---> 6ea5b7975e12
        Successfully built 6ea5b7975e12
        Successfully tagged python-app:latest

    kubectl apply -f manifests/

        clusterrole.rbac.authorization.k8s.io/pods-list created
        clusterrolebinding.rbac.authorization.k8s.io/pods-list created
        configmap/prometheus-config created
        deployment.apps/grafana created
        deployment.apps/prometheus created
        deployment.apps/python-app created
        service/prometheus created

    kubectl get services

        NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
        prometheus   ClusterIP   10.102.131.66   <none>        9090/TCP   2m38s

    kubectl get deployments.apps

        NAME         READY   UP-TO-DATE   AVAILABLE   AGE
        grafana      1/1     1            1           2m16s
        prometheus   1/1     1            1           2m16s
        python-app   1/1     1            1           2m16s

    kubectl get pods --all-namespaces

        NAMESPACE              NAME                                         READY   STATUS      RESTARTS        AGE
        default                grafana-56769656cb-8b6mz                     1/1     Running     0               15m
        default                prometheus-5cdc8c88d8-lhcnk                  1/1     Running     0               15m
        default                python-app-5bd675bd48-6r8wl                  1/1     Running     0               15m
        ingress-nginx          ingress-nginx-admission-create--1-cn7r7      0/1     Completed   1               22h
        ingress-nginx          ingress-nginx-admission-patch--1-m4dww       0/1     Completed   1               22h
        ingress-nginx          ingress-nginx-controller-69bdbc4d57-xqxhs    1/1     Running     0               22h
        kube-system            coredns-78fcd69978-2ffg5                     1/1     Running     0               22h
        kube-system            etcd-minikube                                1/1     Running     7 (22h ago)     22h
        kube-system            kube-apiserver-minikube                      1/1     Running     8 (22h ago)     22h
        kube-system            kube-controller-manager-minikube             1/1     Running     8 (22h ago)     22h
        kube-system            kube-proxy-jbs8b                             1/1     Running     0               22h
        kube-system            kube-scheduler-minikube                      1/1     Running     7 (22h ago)     22h
        kube-system            storage-provisioner                          1/1     Running     2 (3h27m ago)   22h
        kubernetes-dashboard   dashboard-metrics-scraper-5594458c94-psw2w   1/1     Running     0               22h
        kubernetes-dashboard   kubernetes-dashboard-654cf69797-km8wv        1/1     Running     0               22h

    kubectl describe deployments.apps grafana  | grep Port

        Port:       3000/TCP

    kubectl port-forward deployment/grafana 3000:3000

        Forwarding from 127.0.0.1:3000 -> 3000
        Forwarding from [::1]:3000 -> 3000
        Handling connection for 3000

    kubectl delete -f manifests/

        clusterrole.rbac.authorization.k8s.io "pods-list" deleted
        clusterrolebinding.rbac.authorization.k8s.io "pods-list" deleted
        configmap "prometheus-config" deleted
        deployment.apps "grafana" deleted
        deployment.apps "prometheus" deleted
        deployment.apps "python-app" deleted
        service "prometheus" deleted

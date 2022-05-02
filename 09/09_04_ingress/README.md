    minikube addons enable ingress

    minikube addons list

        |-----------------------------|----------|--------------|-----------------------|
        |         ADDON NAME          | PROFILE  |    STATUS    |      MAINTAINER       |
        |-----------------------------|----------|--------------|-----------------------|
        | ambassador                  | minikube | disabled     | unknown (third-party) |
        | auto-pause                  | minikube | disabled     | google                |
        | csi-hostpath-driver         | minikube | disabled     | kubernetes            |
        | dashboard                   | minikube | enabled ✅   | kubernetes            |
        | default-storageclass        | minikube | enabled ✅   | kubernetes            |
        | efk                         | minikube | disabled     | unknown (third-party) |
        | freshpod                    | minikube | disabled     | google                |
        | gcp-auth                    | minikube | disabled     | google                |
        | gvisor                      | minikube | disabled     | google                |
        | helm-tiller                 | minikube | disabled     | unknown (third-party) |
        | ingress                     | minikube | enabled ✅   | unknown (third-party) |
        | ingress-dns                 | minikube | disabled     | unknown (third-party) |
        | istio                       | minikube | disabled     | unknown (third-party) |
        | istio-provisioner           | minikube | disabled     | unknown (third-party) |
        | kubevirt                    | minikube | disabled     | unknown (third-party) |
        | logviewer                   | minikube | disabled     | google                |
        | metallb                     | minikube | disabled     | unknown (third-party) |
        | metrics-server              | minikube | disabled     | kubernetes            |
        | nvidia-driver-installer     | minikube | disabled     | google                |
        | nvidia-gpu-device-plugin    | minikube | disabled     | unknown (third-party) |
        | olm                         | minikube | disabled     | unknown (third-party) |
        | pod-security-policy         | minikube | disabled     | unknown (third-party) |
        | portainer                   | minikube | disabled     | portainer.io          |
        | registry                    | minikube | disabled     | google                |
        | registry-aliases            | minikube | disabled     | unknown (third-party) |
        | registry-creds              | minikube | disabled     | unknown (third-party) |
        | storage-provisioner         | minikube | enabled ✅   | kubernetes            |
        | storage-provisioner-gluster | minikube | disabled     | unknown (third-party) |
        | volumesnapshots             | minikube | disabled     | kubernetes            |
        |-----------------------------|----------|--------------|-----------------------|

    kubectl get pods -n ingress-nginx

        NAME                                        READY   STATUS      RESTARTS        AGE
        ingress-nginx-admission-create--1-cn7r7     0/1     Completed   1               8d
        ingress-nginx-admission-patch--1-m4dww      0/1     Completed   1               8d
        ingress-nginx-controller-69bdbc4d57-xqxhs   1/1     Running     1 (7d14h ago)   8d

    kubectl get pods -n kube-system

        NAME                               READY   STATUS    RESTARTS        AGE
        coredns-78fcd69978-2ffg5           1/1     Running   1 (7d14h ago)   8d
        etcd-minikube                      1/1     Running   8 (7d14h ago)   8d
        kube-apiserver-minikube            1/1     Running   9 (7d14h ago)   8d
        kube-controller-manager-minikube   1/1     Running   9 (7d14h ago)   8d
        kube-proxy-jbs8b                   1/1     Running   1 (7d14h ago)   8d
        kube-scheduler-minikube            1/1     Running   8 (7d14h ago)   8d
        storage-provisioner                1/1     Running   4 (13h ago)     8d

    kubectl apply -f manifests/namespace.yaml

        namespace/tensor created

    kubectl apply -f manifests/

        configmap/configmap-env created
        deployment.apps/my-app created
        ingress.networking.k8s.io/my-ingress created
        namespace/tensor unchanged
        secret/mysql-secret configured
        service/mysql unchanged
        service/nginx unchanged
        statefulset.apps/mysql configured

    kubectl get ingress -n tensor

        NAME         CLASS   HOSTS         ADDRESS          PORTS   AGE
        my-ingress   nginx   my-app.info   192.168.99.101   80      5m52s

    sudo bash -c 'echo "192.168.99.101 my-app.info" >> /etc/hosts'

    ping -c 1 my-app.info

        PING my-app.info (192.168.99.101) 56(84) bytes of data.
        64 bytes from my-app.info (192.168.99.101): icmp_seq=1 ttl=64 time=0.548 ms

        --- my-app.info ping statistics ---
        1 packets transmitted, 1 received, 0% packet loss, time 0ms
        rtt min/avg/max/mdev = 0.548/0.548/0.548/0.000 ms

    kubectl delete -f manifests/

        configmap "configmap-env" deleted
        deployment.apps "my-app" deleted
        ingress.networking.k8s.io "my-ingress" deleted
        namespace "tensor" deleted
        secret "mysql-secret" deleted
        service "mysql" deleted
        service "nginx" deleted
        statefulset.apps "mysql" deleted

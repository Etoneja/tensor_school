    kubectl apply -f manifests/namespace.yaml

        namespace/tensor created
    
    kubectl apply -f manifests/

        namespace/tensor unchanged
        secret/mysql-secret created
        service/mysql created
        statefulset.apps/mysql configured

    kubectl get namespaces

        default                Active   8d
        ingress-nginx          Active   8d
        kube-node-lease        Active   8d
        kube-public            Active   8d
        kube-system            Active   8d
        kubernetes-dashboard   Active   8d
        tensor                 Active   87m

    kubectl get services -n tensor

        NAME    TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
        mysql   ClusterIP   None         <none>        3306/TCP   88m

    kubectl port-forward service/mysql 3306:3306 -n tensor

        Forwarding from 127.0.0.1:3306 -> 3306
        Forwarding from [::1]:3306 -> 3306

    mysql -h 127.0.0.1 -u root -p

        # run init.sql

        mysql> use my_db;
        Database changed

        mysql> select * from articles;
        +----+--------+-------+
        | id | title  | text  |
        +----+--------+-------+
        |  1 | title1 | text1 |
        |  2 | title2 | text2 |
        |  3 | title3 | text3 |
        |  4 | title4 | text4 |
        |  5 | title5 | text5 |
        +----+--------+-------+
        5 rows in set (0,00 sec)

    kubectl delete -f manifests/

        namespace "tensor" deleted
        secret "mysql-secret" deleted
        service "mysql" deleted
        statefulset.apps "mysql" deleted

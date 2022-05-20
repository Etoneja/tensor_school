    helm install . --generate-name

        NAME: chart-1653067377
        LAST DEPLOYED: Fri May 20 20:22:57 2022
        NAMESPACE: default
        STATUS: deployed
        REVISION: 1
        NOTES:
        1. Yo, DAWG:
        Go get your app via: my-app.info

    curl my-app.info


        <!DOCTYPE html>
        <html>
        <body>

        <h1>5. title5</h1>
        <p>text5</p>

        </body>
        </html>

    helm list

        NAME                    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
        chart-1653067377        default         1               2022-05-20 20:22:57.709781386 +0300 MSK deployed        my-app-0.1.0    1.16.0 

    helm uninstall chart-1653067377

        release "chart-1653067377" uninstalled

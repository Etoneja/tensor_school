    eval $(minikube docker-env)

    docker build -t python-app app/

        Sending build context to Docker daemon  5.632kB
        Step 1/7 : FROM python:3.10
        ---> 2b7ca628da40
        Step 2/7 : RUN mkdir -p /app
        ---> Using cache
        ---> ba2f958be0ad
        Step 3/7 : WORKDIR /app
        ---> Using cache
        ---> 7c5ca2bdb957
        Step 4/7 : COPY requirements.txt requirements.txt
        ---> 9b54c964d137
        Step 5/7 : RUN pip install --no-cache-dir -r requirements.txt
        ---> Running in e4a2a65152f0
        Collecting mysql-connector-python==8.0.29
        Downloading mysql_connector_python-8.0.29-cp310-cp310-manylinux1_x86_64.whl (25.2 MB)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 25.2/25.2 MB 2.3 MB/s eta 0:00:00
        Collecting protobuf>=3.0.0
        Downloading protobuf-3.20.1-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.1 MB)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 3.0 MB/s eta 0:00:00
        Installing collected packages: protobuf, mysql-connector-python
        Successfully installed mysql-connector-python-8.0.29 protobuf-3.20.1
        Removing intermediate container e4a2a65152f0
        ---> 63f58c30ef36
        Step 6/7 : COPY . .
        ---> e9e6fcf5dcb6
        Step 7/7 : CMD ["python", "app.py"]
        ---> Running in e372dcdc2e91
        Removing intermediate container e372dcdc2e91
        ---> 38f6198e7d53
        Successfully built 38f6198e7d53
        Successfully tagged python-app:latest

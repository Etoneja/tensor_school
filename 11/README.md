    docker-compose up -d

        Building backend
        Sending build context to Docker daemon  7.168kB
        Step 1/6 : FROM python:3.10-alpine
        ---> f7605eb83caf
        Step 2/6 : COPY requirements.txt /
        ---> 87837d3a15be
        Step 3/6 : RUN pip install --no-cache-dir -r requirements.txt
        ---> Running in 02d0f3e46520
        Collecting tornado==6.1
        Downloading tornado-6.1.tar.gz (497 kB)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 497.4/497.4 KB 1.5 MB/s eta 0:00:00
        Preparing metadata (setup.py): started
        Preparing metadata (setup.py): finished with status 'done'
        Building wheels for collected packages: tornado
        Building wheel for tornado (setup.py): started
        Building wheel for tornado (setup.py): finished with status 'done'
        Created wheel for tornado: filename=tornado-6.1-cp310-cp310-linux_x86_64.whl size=414482 sha256=5a6e9585c03978e11583df22aba06dc97773163357f90d6dfe6e490ab908cbb7
        Stored in directory: /tmp/pip-ephem-wheel-cache-7asoo_5o/wheels/80/32/8d/21cf0fa6ee4e083f6530e5b83dfdfa9489a3890d320803f4c7
        Successfully built tornado
        Installing collected packages: tornado
        Successfully installed tornado-6.1
        WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
        WARNING: You are using pip version 22.0.4; however, version 22.1.1 is available.
        You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
        Removing intermediate container 02d0f3e46520
        ---> 7745a44f8c5f
        Step 4/6 : COPY src/ /app
        ---> 661085f6346d
        Step 5/6 : WORKDIR /app
        ---> Running in 740e478e76a1
        Removing intermediate container 740e478e76a1
        ---> 88124c762c48
        Step 6/6 : CMD ["python", "index.py"]
        ---> Running in 841491e1c4bd
        Removing intermediate container 841491e1c4bd
        ---> 400e05fbfb59
        Successfully built 400e05fbfb59
        Successfully tagged 11_backend:latest
        WARNING: Image for service backend was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
        Building service
        Sending build context to Docker daemon  6.656kB
        Step 1/6 : FROM python:3.10-alpine
        ---> f7605eb83caf
        Step 2/6 : COPY requirements.txt /
        ---> b8dca43deb31
        Step 3/6 : RUN pip install --no-cache-dir -r requirements.txt
        ---> Running in 6a964a205f1c
        Collecting httpx>=0.19
        Downloading httpx-0.23.0-py3-none-any.whl (84 kB)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.8/84.8 KB 1.5 MB/s eta 0:00:00
        Collecting httpcore<0.16.0,>=0.15.0
        Downloading httpcore-0.15.0-py3-none-any.whl (68 kB)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 68.4/68.4 KB 1.8 MB/s eta 0:00:00
        Collecting sniffio
        Downloading sniffio-1.2.0-py3-none-any.whl (10 kB)
        Collecting certifi
        Downloading certifi-2022.5.18.1-py3-none-any.whl (155 kB)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.2/155.2 KB 1.8 MB/s eta 0:00:00
        Collecting rfc3986[idna2008]<2,>=1.3
        Downloading rfc3986-1.5.0-py2.py3-none-any.whl (31 kB)
        Collecting h11<0.13,>=0.11
        Downloading h11-0.12.0-py3-none-any.whl (54 kB)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.9/54.9 KB 2.1 MB/s eta 0:00:00
        Collecting anyio==3.*
        Downloading anyio-3.6.1-py3-none-any.whl (80 kB)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80.6/80.6 KB 2.0 MB/s eta 0:00:00
        Collecting idna>=2.8
        Downloading idna-3.3-py3-none-any.whl (61 kB)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 KB 2.2 MB/s eta 0:00:00
        Installing collected packages: rfc3986, sniffio, idna, h11, certifi, anyio, httpcore, httpx
        Successfully installed anyio-3.6.1 certifi-2022.5.18.1 h11-0.12.0 httpcore-0.15.0 httpx-0.23.0 idna-3.3 rfc3986-1.5.0 sniffio-1.2.0
        WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
        WARNING: You are using pip version 22.0.4; however, version 22.1.1 is available.
        You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
        Removing intermediate container 6a964a205f1c
        ---> d8c5796b5c21
        Step 4/6 : COPY src/ /app
        ---> 1682bd376f6e
        Step 5/6 : WORKDIR /app
        ---> Running in 08785c370a12
        Removing intermediate container 08785c370a12
        ---> 20503f888e5d
        Step 6/6 : CMD ["python", "index.py"]
        ---> Running in 10da932522b5
        Removing intermediate container 10da932522b5
        ---> 64cafe10acb8
        Successfully built 64cafe10acb8
        Successfully tagged 11_service:latest
        WARNING: Image for service service was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
        Creating 11_service_1 ... done
        Creating 11_backend_1 ... done

    docker-compose ps

            Name           Command       State                    Ports                  
        ---------------------------------------------------------------------------------
        11_backend_1   python index.py   Up      0.0.0.0:8888->8888/tcp,:::8888->8888/tcp
        11_service_1   python index.py   Up
    
    docker-compose logs

        Attaching to 11_backend_1, 11_service_1
        backend_1  | [I 220529 10:25:25 index:33] Request 6f998dcd-44b3-4a71-82b9-1f15d25aa059 started
        backend_1  | [I 220529 10:25:38 web:2239] 200 GET / (172.30.0.2) 13014.29ms
        backend_1  | [I 220529 10:25:38 index:44] Request 6f998dcd-44b3-4a71-82b9-1f15d25aa059 finished
        backend_1  | [I 220529 10:25:43 index:33] Request 64948605-2642-4b63-93e9-f67a1c7723af started
        backend_1  | [I 220529 10:25:56 web:2239] 200 GET / (172.30.0.2) 13015.27ms
        backend_1  | [I 220529 10:25:56 index:44] Request 64948605-2642-4b63-93e9-f67a1c7723af finished
        backend_1  | [I 220529 10:26:01 index:33] Request 5406d8d9-5bc9-432d-955f-6001ef1b04ff started
        backend_1  | [I 220529 10:26:14 web:2239] 200 GET / (172.30.0.2) 13011.72ms
        backend_1  | [I 220529 10:26:14 index:44] Request 5406d8d9-5bc9-432d-955f-6001ef1b04ff finished
        backend_1  | [I 220529 10:26:19 index:33] Request 0ba26f6f-c2f5-4d04-94a2-e4fbed6537f6 started
        backend_1  | [I 220529 10:26:32 web:2239] 200 GET / (172.30.0.2) 13010.73ms
        backend_1  | [I 220529 10:26:32 index:44] Request 0ba26f6f-c2f5-4d04-94a2-e4fbed6537f6 finished
        backend_1  | [I 220529 10:26:37 index:33] Request 955481a3-43ce-4cac-ab18-d487e72f5c08 started
        service_1  | 2022-05-29 10:25:25 INFO     Service started
        service_1  | 2022-05-29 10:25:25 DEBUG    Service step 1
        service_1  | 2022-05-29 10:25:25 DEBUG    Performing request to endpoint http://backend:8888/ with timeout 15
        service_1  | 2022-05-29 10:25:38 INFO     Request result: {'res': '2022-05-29 10:25:25.042222'}
        service_1  | 2022-05-29 10:25:43 DEBUG    Service step 2
        service_1  | 2022-05-29 10:25:43 DEBUG    Performing request to endpoint http://backend:8888/ with timeout 15
        service_1  | 2022-05-29 10:25:56 INFO     Request result: {'res': '2022-05-29 10:25:43.081120'}
        service_1  | 2022-05-29 10:26:01 DEBUG    Service step 3
        service_1  | 2022-05-29 10:26:01 DEBUG    Performing request to endpoint http://backend:8888/ with timeout 15
        service_1  | 2022-05-29 10:26:14 INFO     Request result: {'res': '2022-05-29 10:26:01.137156'}
        service_1  | 2022-05-29 10:26:19 DEBUG    Service step 4
        service_1  | 2022-05-29 10:26:19 DEBUG    Performing request to endpoint http://backend:8888/ with timeout 15
        service_1  | 2022-05-29 10:26:32 INFO     Request result: {'res': '2022-05-29 10:26:19.172886'}
        service_1  | 2022-05-29 10:26:37 DEBUG    Service step 5
        service_1  | 2022-05-29 10:26:37 DEBUG    Performing request to endpoint http://backend:8888/ with timeout 15

    docker-compose down

        Stopping 11_backend_1 ... done
        Stopping 11_service_1 ... done
        Removing 11_backend_1 ... done
        Removing 11_service_1 ... done
        Removing network 11_default

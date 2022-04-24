FROM python:3.10 
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 9080
CMD ["python", "exporter.py"]

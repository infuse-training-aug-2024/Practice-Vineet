
FROM python:3


WORKDIR /app


RUN mkdir -p /app/output


COPY . .


RUN pip install --no-cache-dir -r requirements.txt


ENV GREETING="Hello from Docker!"


CMD ["python", "script.py", "1", "2", "3", "4"]

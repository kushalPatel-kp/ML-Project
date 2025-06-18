FROM python:3.11.13-slim
WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y
RUN pip install -r requirenment.txt
CMD ["python3", "app.py"]

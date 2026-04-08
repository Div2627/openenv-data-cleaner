FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# This ensures the container stays running
CMD ["python", "-c", "import time; print('Environment Running...'); [time.sleep(10) for _ in iter(int, 1)]"]

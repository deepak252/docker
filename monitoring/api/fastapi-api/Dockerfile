FROM python:3.12-alpine

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir fastapi uvicorn

# Disable access logs and set log level to critical
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--no-access-log"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--no-access-log", "--log-level", "error"]

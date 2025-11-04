from fastapi import FastAPI
from celery import Celery

celery = Celery("tasks", broker="amqp://guest:guest@rabbitmq:5672//")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Celery with RabbitMQ and FastAPI"}

@app.post("/send-email/{email}")
def send_email_task(email: str):
    # Send a task by name (it will be consumed by Celery worker)
    celery.send_task("tasks.send_email_task", args=[email])
    return {"status": "queued", "email": email}

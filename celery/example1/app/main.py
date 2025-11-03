from fastapi import FastAPI
from tasks import send_email

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Celery with RabbitMQ and FastAPI"}

@app.post("/send-email/{email}")
def send_email_task(email: str):
    # sends the task to Celery asynchronously.
    # .delay() pushes the task message to RabbitMQ via the Celery broker. It immediately returns without blocking.
    send_email.delay(email)
    return {"status": "queued", "email": email}

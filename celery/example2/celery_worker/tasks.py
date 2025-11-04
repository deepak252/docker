from celery import Celery
import time

celery = Celery(
    "tasks", 
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="db+postgresql://root:root@db/test_db"
)

# Declares this function as a Celery task.
# Celery registers this function so it can be called asynchronously by workers.
@celery.task(name="tasks.send_email_task")
def send_email(email):
    print(f"📨 Sending email to {email}...")
    time.sleep(5)
    print(f"✅ Email sent to {email}")
    # Returns a confirmation message.
    # Celery can store this result in the backend (rpc:// here).
    return f"Email sent to {email}"

from celery_app import celery
import time

# Declares this function as a Celery task.
# Celery registers this function so it can be called asynchronously by workers.
@celery.task
def send_email(email):
    print(f"📨 Sending email to {email}...")
    time.sleep(5)
    print(f"✅ Email sent to {email}")
    # Returns a confirmation message.
    # Celery can store this result in the backend (rpc:// here).
    return f"Email sent to {email}"
    
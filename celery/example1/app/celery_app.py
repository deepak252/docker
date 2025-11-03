from celery import Celery

# Creates a Celery app instance.
# Every Celery worker or producer uses this app to send or receive tasks.
# "tasks" is just a name for this app (like a namespace).
# broker-The broker is RabbitMQ — this tells Celery where to send/receive task messages.
# backend- Defines where Celery stores results of tasks.
celery = Celery(
    "tasks",
    broker="amqp://guest:guest@rabbitmq:5672//",
    # broker="amqp://guest:guest@localhost:5672//",
    # backend="rpc://"          
)

# # Tells Celery to route all tasks from the tasks module to a queue named "default".
# # This gives you control over which tasks go to which queue (useful for scaling).
# celery.conf.task_routes = {"tasks.*": {"queue": "default"}}
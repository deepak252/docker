from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')
# app = Celery('tasks', 'amqp://guest:guest@rabbitmq:5672//')

@app.task
def add(x, y):
    print(f'Task: {x} + {y} = {x+y}')
    return x+y
from celery import Celery


app = Celery(
    "tasks",
    broker="amqp://192.168.0.12:5672",
    include=["core.bot_tasks", "core.test_tasks"],
)

import logging
from time import sleep

from celery import Celery


app = Celery("tasks", broker="amqp://localhost:5672")


@app.task()
def slow_hello_world() -> str:
    logging.info("Starting the task")
    sleep(10)
    logging.info("Stoping the task")
    return "Hello, World!"


@app.task()
def do_operation_on_calculator_and_record_result(operation: str) -> None:
    logging.info("Starting the task")
    sleep(1)
    logging.info("Opening calculator")
    sleep(1)
    logging.info(f"Doing operation {operation}")
    sleep(1)
    logging.info("Recording result")
    sleep(1)


@app.task()
def get_main_news_of_ge_and_record_result() -> None:
    logging.info("Starting the task")
    sleep(1)
    logging.info("Opening site")
    sleep(1)
    logging.info(f"Getting titles of main news")
    sleep(1)
    logging.info("Recording result")
    sleep(1)

import logging
from time import sleep

from .celery import app


@app.task
def slow_hello_world(sleep_time: int = 10) -> str:
    logging.info("Starting the task")
    sleep(sleep_time)
    logging.info("Stoping the task")
    return "Hello, World!"


@app.task
def return_something(something: str = "Another task created succesfully") -> str:
    logging.info("Starting the task")
    logging.info("Stoping the task")
    return something

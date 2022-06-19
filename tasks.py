import logging
from time import sleep
from pathlib import Path
from subprocess import Popen

from celery import Celery

from selenium.webdriver import Remote
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


app = Celery("tasks", broker="amqp://192.168.0.12:5672")

results_path = Path(__file__).parent.resolve() / "results"


@app.task()
def slow_hello_world(sleep_time: int = 10) -> str:
    logging.info("Starting the task")
    sleep(sleep_time)
    logging.info("Stoping the task")
    return "Hello, World!"


@app.task()
def do_operation_on_calculator_and_record_result(operation: str) -> None:
    logging.info("Initialing driver server")
    driver_server = Popen("WinAppDriver.exe")
    driver = Remote(
        "http://localhost:4723",
        desired_capabilities={
            "automationName": "Windows",
            "platformName": "Windows",
            "app": "Root",
        },
    )
    wait = WebDriverWait(driver, 30)

    logging.info("Opening calculator")
    calc_process = Popen("calc.exe")
    calc_app = wait.until(ec.element_to_be_clickable((By.NAME, "Calculator")))

    logging.info(f"Doing operation {operation}")
    calc_app.find_element(By.NAME, "Clear").send_keys(Keys.SPACE)
    calc_app.send_keys(operation)

    logging.info("Capturing and recording result")
    driver.save_screenshot(str(results_path / "calc_result.png"))

    logging.info("Closing app")
    calc_app.send_keys(Keys.ALT + Keys.F4)
    calc_process.terminate()
    driver_server.terminate()


@app.task()
def get_website_screenshot(url: str) -> None:

    logging.info("Initialing WebDriver")
    driver = Chrome()

    logging.info("Opening site")
    driver.get(url)

    logging.info("Capturing and recording result")
    driver.save_screenshot(str(results_path / "ge_result.png"))

    logging.info("Closing app")
    driver.quit()

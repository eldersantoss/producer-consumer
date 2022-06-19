import logging

from core import test_tasks, bot_tasks


if __name__ == "__main__":
    logging.info("Starting distributed app")

    test_tasks.slow_hello_world()
    test_tasks.return_something()

    bot_tasks.do_operation_on_calculator_and_record_result("7*9=")
    bot_tasks.get_website_screenshot("https://ge.globo.com")

    logging.info("Stoping distributed app")

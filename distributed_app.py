import logging

import tasks


if __name__ == "__main__":
    logging.info("Starting distributed app")
    tasks.slow_hello_world.delay()
    tasks.do_operation_on_calculator_and_record_result.delay("7*9=")
    tasks.get_website_screenshot.delay("https://ge.globo.com")
    logging.info("Stoping distributed app")

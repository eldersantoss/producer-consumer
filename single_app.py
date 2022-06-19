import logging

import tasks


if __name__ == "__main__":
    logging.info("Starting single app")
    tasks.slow_hello_world()
    tasks.do_operation_on_calculator_and_record_result("7*9=")
    tasks.get_website_screenshot("https://ge.globo.com")
    logging.info("Stoping single app")

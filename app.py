import logging

import tasks


def main():
    logging.info("Starting app")
    tasks.slow_hello_world.delay()
    tasks.do_operation_on_calculator_and_record_result.delay("7*9")
    tasks.get_main_news_of_ge_and_record_result.delay()
    logging.info("Stoping app")


if __name__ == "__main__":
    main()

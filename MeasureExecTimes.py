import time
import logging
from functools import wraps


def measure_execution_time(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fun(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time

    return wrapper


def add_logging(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        # Set up logging
        logging.basicConfig(filename='function_calls.log', level=logging.INFO)
        logger = logging.getLogger(__name__)

        # Get current date and time
        current_datetime = time.strftime('%Y-%m-%d %H:%M:%S')

        # Log the function name and arguments
        logger.info(f"Function: {fun.__name__}, Arguments: {args}, Keyword Arguments: {kwargs}")

        # Call the function and measure execution time
        result, execution_time = measure_execution_time(fun)(*args, **kwargs)

        # Log the function result and execution time
        logger.info(
            f"[{current_datetime}] Function: {fun.__name__}, Result: {result}, Execution Time: {execution_time} seconds")

        return result, execution_time

    return wrapper

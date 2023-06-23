import time
from functools import wraps

def measure_execution_time(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fun(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # Print the function name, similarity result, and execution time
        print(fun.__name__, ":", result)
        print("time:", execution_time)

        return result, execution_time
    return wrapper
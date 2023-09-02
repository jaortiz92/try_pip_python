import time

def time_execution(function):
    def function_time(*arg, **kwargs):
        start = time.time()
        c = function(*arg, **kwargs)
        end = time.time()
        interval = end - start
        return [interval, c]
    return function_time

def time_execution_print(function):
    def function_time(*arg, **kwargs):
        start = time.time()
        c = function(*arg, **kwargs)
        end = time.time()
        interval = end - start
        print(interval)
        return c
    return function_time

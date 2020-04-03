from functools import wraps

def my_logger(org_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(org_func.__name__), level=logging.INFO)

    @wraps(org_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return org_func(*args, **kwargs)

    return wrapper

def my_timer(org_func):
    import time

    @wraps(org_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = org_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(org_func.__name__, t2))
        return result

    return wrapper

@my_logger
@my_timer # means display_info = my_logger(my_timer(display_info))
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Abhishek', 21)
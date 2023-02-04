import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} was {time.time() - start} seconds')
        return result
    return wrapper


@measure_time
def operation():
    print('Starting operation')
    time.sleep(1)
    print('Operation finished')
    return 123


if __name__ == '__main__':
    operation()

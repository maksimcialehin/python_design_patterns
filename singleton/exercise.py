def is_singleton(factory):
    # call factory() and return true or false
    # depending on whether the factory makes a singleton or not
    return factory() is factory()

import signal


def timeout_handler(signum, frame):
    raise TimeoutError('Timeout!')


def initialize():
    # Initialize the signal handler
    signal.signal(signal.SIGALRM, timeout_handler)
    print('Initialized!')
    return True

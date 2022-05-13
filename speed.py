import time
import signal
import requests
from tqdm import tqdm
from tools import get_file_size_unit


def benchmark(files_list, files_type='tiny', timeout=0):
    file_size = 0  # Bytes
    time_cost = 0  # seconds
    if not timeout:
        timeout = 5 if files_type.lower() == 'tiny' else 120

    progress = tqdm(files_list)
    for file in progress:
        progress.set_description(f"Downloading {file}")
        try:
            signal.alarm(timeout)
            start_time = time.perf_counter()
            r = requests.get(file, timeout=timeout)
            end_time = time.perf_counter()
        except:
            signal.alarm(0)
            return 0, 0
        finally:
            signal.alarm(0)
        if r.status_code == 200:
            file_size += len(r.content)
            time_cost += end_time - start_time
    time_cost_string = f'{time_cost * 1000:.3f} ms' if time_cost < 1 else f'{time_cost:.3f} s'
    print(f"Downloaded {get_file_size_unit(file_size)[0]:.2f} {get_file_size_unit(file_size)[1]} in {time_cost_string}")
    return file_size, time_cost

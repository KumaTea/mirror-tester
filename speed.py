import math
import time
import signal
import requests
from tqdm import tqdm
from tools import get_file_size_unit


def benchmark(files_list, files_type='tiny', timeout=0):
    # file_size = 0  # Bytes
    # time_cost = 0  # seconds
    if not timeout:
        timeout = 5 if files_type.lower() == 'tiny' else 120

    progress = tqdm(files_list)
    results = []
    for file in progress:
        progress.set_description(f"  Downloading {file[-20:]}")
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
            file_size = len(r.content)
            time_cost = end_time - start_time
            results.append([file_size, time_cost])
    if not results:
        return 0, 0
    if len(results) > 5:
        results.sort(key=lambda x: x[0] / x[1])
        results = results[math.ceil(len(results) * 0.1):math.floor(len(results) * 0.9)]
    total_size = sum([result[0] for result in results])
    total_time = sum([result[1] for result in results])
    time_cost_string = f'{total_time * 1000:.3f} ms' if total_time < 1 else f'{total_time:.3f} s'
    print(f"  Downloaded {get_file_size_unit(total_size)[0]:.2f} {get_file_size_unit(total_size)[1]} in {time_cost_string}")
    return total_size, total_time

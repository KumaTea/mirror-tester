import time
import requests
from tqdm import tqdm
from tools import get_file_size_unit


def benchmark(files_list):
    file_size = 0  # Bytes
    time_cost = 0  # seconds

    progress = tqdm(files_list)
    for file in progress:
        progress.set_description(f"Downloading {file}")
        start_time = time.perf_counter()
        r = requests.get(file)
        end_time = time.perf_counter()
        if r.status_code == 200:
            file_size += len(r.content)
            time_cost += end_time - start_time

    time_cost_string = f'{time_cost * 1000:.3f} ms' if time_cost < 1 else f'{time_cost:.3f} s'
    print(f"Downloaded {get_file_size_unit(file_size)[0]:.2f} {get_file_size_unit(file_size)[1]} in {time_cost_string}")
    return file_size, time_cost

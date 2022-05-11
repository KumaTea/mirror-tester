import requests
from tqdm import tqdm
from ping import ping
from speed import benchmark
from tools import get_file_size_unit
from configparser import ConfigParser
from gen_files import tiny_file_total_size, large_file_total_size


def get_test_repos():
    repos = []
    config = ConfigParser()
    config.read('data/config.ini')
    for section in config.sections():
        repos.append(section)
    return repos


def get_test_files(repo, files_type):
    files = []
    with open(f'data/{repo}_{files_type}.txt') as f:
        for line in f:
            files.append(line.strip())
    return files


def get_speed_points(file_size, time_cost):
    max_speed = 1024 * 1024 * 100  # 100MB/s
    speed = file_size / time_cost  # Bytes/s
    bps = get_file_size_unit(speed * 8)
    print(f'Download speed: {bps[0]:.2f} {bps[1][:1]}bps')
    if speed > max_speed:
        return 100
    else:
        return speed / max_speed * 100


def test_mirror(mirror_url):
    # Test the quality of the mirror
    print("Testing mirror:", mirror_url)

    # Ping test
    domain = mirror_url.replace('https://', '').replace('http://', '').replace('/', '')
    print("[1/4] Pinging", domain)
    ping_point = 0
    ping_result = ping(domain)
    if ping_result:
        print(f'Ping result: {ping_result} ms')
        ping_point = 100.0 - ping_result
    else:
        ping_result = 'Failed'
        print("Ping test failed")

    repos = get_test_repos()

    # Mirror richness test
    print("[2/4] Available repos test")
    available_repos = []
    for repo in tqdm(repos):
        try:
            r = requests.get(f'{mirror_url}/{repo}/', timeout=5)
            if r.status_code == 200:
                available_repos.append(repo)
        except:
            pass
    mirror_richness_point = len(available_repos) / len(repos) * 100
    richness_result = f'{len(available_repos)}/{len(repos)}'

    # Tiny files download test
    print("[3/4] Tiny files test")
    # tiny_files_point = 0
    tiny_files_total_point = 0
    tiny_files_test_count = 0
    tiny_files_total_size = 0
    tiny_files_total_time = 0
    for repo in available_repos:
        files = get_test_files(repo, 'tiny')
        file_urls = [f'{mirror_url}/{repo}/{file}' for file in files]
        file_size, time_cost = benchmark(file_urls, 'tiny')
        if file_size > tiny_file_total_size / 4:
            test_point = get_speed_points(file_size, time_cost)
        else:
            test_point = 0
        if test_point:
            tiny_files_total_point += test_point
            tiny_files_test_count += 1
            tiny_files_total_size += file_size
            tiny_files_total_time += time_cost
    if tiny_files_test_count:
        tiny_files_point = 1024 * tiny_files_total_point / tiny_files_test_count
        tiny_files_point = 100 if tiny_files_point > 100 else tiny_files_point
        tiny_files_speed, tiny_files_unit = get_file_size_unit(tiny_files_total_size / tiny_files_total_time)
        tiny_files_speed_str = f'{tiny_files_speed:.2f} {tiny_files_unit[0]}B/s'
    else:
        tiny_files_point = 0
        tiny_files_speed_str = '0 B/s'

    # Large files download test
    print("[4/4] Large files test")
    # large_files_point = 0
    large_files_total_point = 0
    large_files_test_count = 0
    large_files_total_size = 0
    large_files_total_time = 0
    for repo in available_repos:
        files = get_test_files(repo, 'large')
        file_urls = [f'{mirror_url}/{repo}/{file}' for file in files]
        file_size, time_cost = benchmark(file_urls, 'large')
        if file_size > large_file_total_size / 4:
            test_point = get_speed_points(file_size, time_cost)
        else:
            test_point = 0
        if test_point:
            large_files_total_point += test_point
            large_files_test_count += 1
            large_files_total_size += file_size
            large_files_total_time += time_cost
    if large_files_test_count:
        large_files_point = large_files_total_point / large_files_test_count
        large_files_speed, large_files_unit = get_file_size_unit(large_files_total_size / large_files_total_time)
        large_files_speed_str = f'{large_files_speed:.2f} {large_files_unit[0]}B/s'
    else:
        large_files_point = 0
        large_files_speed_str = '0 B/s'

    final_points = 0
    final_points += ping_point * (10 / 100)
    final_points += tiny_files_point * (50 / 100)
    final_points += large_files_point * (30 / 100)
    final_points += mirror_richness_point * (10 / 100)
    final_points_str = f'{final_points:.2f}'
    print(f'Final points: {final_points_str}')

    return final_points_str, ping_result, tiny_files_speed_str, large_files_speed_str, richness_result

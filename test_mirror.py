import random
import signal
import requests
from config import *
from tqdm import tqdm
from ping import min_ping
from speed import benchmark
from mirrors import all_mirrors
from tools import get_file_size_unit
from configparser import ConfigParser
from gen_files import tiny_file_total_size, large_file_total_size


def get_test_repos():
    test_repos = []
    config = ConfigParser()
    config.read('data/config.ini')
    for section in config.sections():
        test_repos.append(section)
    return test_repos


def get_test_files(repo, files_type):
    files = []
    with open(f'data/{repo}_{files_type}.txt') as f:
        for line in f:
            files.append(line.strip())
    return files


def get_speed_points(file_size, time_cost, test_item='tiny'):
    if test_item == 'tiny':
        max_speed = tiny_max_speed
    else:
        max_speed = large_max_speed
    try:
        speed = file_size / time_cost  # Bytes/s
    except ZeroDivisionError:
        speed = 0
    bytes_count, unit = get_file_size_unit(speed * 8)
    unit_str = f'{unit[:1]}bps' if not unit.startswith('B') else 'bps'
    print(f'  Download speed: {bytes_count:.2f} {unit_str}')
    if speed > max_speed:
        return 100
    else:
        return speed / max_speed * 100


def test_mirror(mirror):
    mirror_url = all_mirrors[mirror]['url']
    # Test the quality of the mirror
    print("Testing mirror:", mirror_url)

    # Ping test
    domain = mirror_url.replace('https://', '').replace('http://', '').replace('/', '')
    print("[1/4] Pinging", domain)
    ping_point = 0
    ping_result = min_ping(domain)
    if ping_result:
        print(f'  Ping result: {ping_result} ms')
        ping_point = max([100.0 - ping_result, 0.])
    else:
        ping_result = 'Failed'
        print("  Ping test failed")

    repos = get_test_repos()

    # Mirror richness test
    print("[2/4] Available repos test")
    available_repos = []
    for repo in tqdm(repos):
        repo_path = all_mirrors[mirror]['special'][repo] if repo in all_mirrors[mirror]['special'] else repo
        try:
            signal.alarm(avail_test_timeout)
            r = requests.get(f'{mirror_url}/{repo_path}/', timeout=avail_test_timeout)
            if r.status_code == 200:
                available_repos.append(repo)
            signal.alarm(0)
        except:
            print(f'  {repo} is not available')
            pass
        finally:
            signal.alarm(0)
    mirror_richness_point = len(available_repos) / len(repos) * 100
    richness_result = f'{len(available_repos)}/{len(repos)}'

    # prepare repos for download test
    download_repos = random.sample(available_repos, repo_samples) if len(available_repos) > repo_samples else available_repos

    # Tiny files download test
    print("[3/4] Tiny files test")
    # tiny_files_point = 0
    tiny_files_total_point = 0
    tiny_files_test_count = 0
    tiny_files_total_size = 0
    tiny_files_total_time = 0
    for repo in download_repos:
        files = random.sample(get_test_files(repo, 'tiny'), tiny_files_samples)
        repo_path = all_mirrors[mirror]['special'][repo] if repo in all_mirrors[mirror]['special'] else repo
        file_urls = [f'{mirror_url}/{repo_path}/{file}' for file in files]
        file_size, time_cost = benchmark(file_urls, 'tiny', tiny_test_timeout)

        test_point = get_speed_points(file_size, time_cost, 'tiny')
        if test_point:
            tiny_files_total_point += test_point
            tiny_files_test_count += 1
            tiny_files_total_size += file_size
            tiny_files_total_time += time_cost
    if tiny_files_test_count:
        tiny_files_point = tiny_files_total_point / tiny_files_test_count
        tiny_files_point = 100 if tiny_files_point > 100 else tiny_files_point
        tiny_files_speed, tiny_files_unit = get_file_size_unit(tiny_files_total_size / tiny_files_total_time)
        tiny_files_unit_str = f'{tiny_files_unit[0]}B/s' if not tiny_files_unit.startswith('B') else 'B/s'
        tiny_files_speed_str = f'{tiny_files_speed:.2f} {tiny_files_unit_str}'
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
    for repo in download_repos:
        files = random.sample(get_test_files(repo, 'large'), large_files_samples)
        repo_path = all_mirrors[mirror]['special'][repo] if repo in all_mirrors[mirror]['special'] else repo
        file_urls = [f'{mirror_url}/{repo_path}/{file}' for file in files]
        file_size, time_cost = benchmark(file_urls, 'large', large_test_timeout)

        test_point = get_speed_points(file_size, time_cost, 'large')
        if test_point:
            large_files_total_point += test_point
            large_files_test_count += 1
            large_files_total_size += file_size
            large_files_total_time += time_cost
    if large_files_test_count:
        large_files_point = large_files_total_point / large_files_test_count
        large_files_point = 100 if large_files_point > 100 else large_files_point
        large_files_speed, large_files_unit = get_file_size_unit(large_files_total_size / large_files_total_time)
        large_files_unit_str = f'{large_files_unit[0]}B/s' if not large_files_unit.startswith('B') else 'B/s'
        large_files_speed_str = f'{large_files_speed:.2f} {large_files_unit_str}'
    else:
        large_files_point = 0
        large_files_speed_str = '0 B/s'

    final_points = 0
    final_points += ping_point            * (rates['ping']  / 100)
    final_points += tiny_files_point      * (rates['tiny']  / 100)
    final_points += large_files_point     * (rates['large'] / 100)
    final_points += mirror_richness_point * (rates['rich']  / 100)
    final_points_str = f'{final_points:.2f}'
    print(f'Final points: {final_points_str}')

    return final_points_str, ping_result, tiny_files_speed_str, large_files_speed_str, richness_result

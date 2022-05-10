# Files list generator

import os
import sys
import random
from search import recurse_search
from configparser import ConfigParser


tiny_file_min = 1.0  # KiB
tiny_file_max = 25.0  # KiB
large_file_min = 25.0  # MiB
large_file_max = 125.0  # MiB

tiny_file_count = 100
large_file_count = 10

tiny_file_total_size = 1250.0  # KiB
tiny_file_total_size_delta = 50.0  # KiB
large_file_total_size = 750.0  # MiB
large_file_total_size_delta = 25.0  # MiB


def pick_files(file_list, file_count, total_size, total_size_delta):
    tries = 0
    while True:
        tries += 1
        files = random.sample(file_list, file_count)
        file_sizes = [file[1] for file in files]
        if abs(total_size - sum(file_sizes)) < total_size_delta:
            break
        else:
            if tries % 100 == 0:
                sys.stdout.write('\rTries: {}, size: {}'.format(tries, sum(file_sizes)))
                total_size_delta += 0.1
    print(f'Tries: {tries}')
    print(f'Size: {sum(file_sizes)}\n')
    return [file[0] for file in files]


def main(repo=None, urls=None):
    repo = repo or input('Repository: ')
    # if repo not in repositories:
    #     raise ValueError(f'Repository {repo} not found\n Available repositories: {list(repositories.keys())}')
    urls = urls or input("Enter URL, split by comma: ")
    url_list = urls.split(",")

    files = []
    tiny_files = []
    large_files = []

    for url in url_list:
        print(f'\nProcessing: {url}')
        files.extend(recurse_search(url))

    for file in files:
        link = file[0]
        size_str = file[1]
        size = size_str.split(' ')[0]
        unit = size_str.split(' ')[1]
        if unit == 'KiB':
            if tiny_file_min <= float(size) <= tiny_file_max:
                tiny_files.append((link, float(size)))
        else:  # elif unit == 'MiB':
            if large_file_min <= float(size) <= large_file_max:
                large_files.append((link, float(size)))

    tiny_files = list(set(tiny_files))
    large_files = list(set(large_files))

    print(f'Picking tiny files...')
    picked_tiny_files = pick_files(tiny_files, tiny_file_count, tiny_file_total_size, tiny_file_total_size_delta)
    print(f'Picking large files...')
    picked_large_files = pick_files(large_files, large_file_count, large_file_total_size, large_file_total_size_delta)

    # print("Tiny files:")
    # for file in tiny_files:
    #     print(f'\'{file}\',')
    with open(f'data/{repo}_tiny.txt', 'w') as f:
        f.write('\n'.join([file.replace(
            picked_tiny_files[0][:picked_tiny_files[0].find(repo) + len(f'{repo}/')], ''
        ) for file in picked_tiny_files]))
    # print("Large files:")
    # for file in large_files:
    #     print(f'\'{file}\',')
    with open(f'data/{repo}_large.txt', 'w') as f:
        f.write('\n'.join([file.replace(
            picked_large_files[0][:picked_large_files[0].find(repo) + len(f'{repo}/')], ''
        ) for file in picked_large_files]))
    return print('Done')


if __name__ == '__main__':
    interactive = input('Interactive? (y/n): ')
    if interactive.lower() == 'y':
        main()
    else:
        config = ConfigParser()
        config.read('data/config.ini')
        for i in config.sections():
            if not os.path.isfile(f'data/{i}_tiny.txt') or not os.path.isfile(f'data/{i}_large.txt'):
                print(f'Processing {i}')
                main(i, config[i]['urls'])
            else:
                print(f'Skipping {i}')

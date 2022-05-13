import os
import csv
from mirrors import *


results_path = 'results'


def read_results(path):
    results = {}
    results_files = []
    for file in os.listdir(path):
        if file.endswith('.txt'):
            results_files.append(file)
    for file in results_files:
        repo = file.split('.')[0]
        with open(os.path.join(path, file), 'r') as f:
            result = f.read().split('\n')
        results[repo] = {
            'points': result[0].split(': ')[1],
            'ping': result[1].split(': ')[1],
            'tiny_speed': result[2].split(': ')[1],
            'large_speed': result[3].split(': ')[1],
            'richness': result[4].split(': ')[1]
        }
    return results


def sort_results(results):
    # sort results by points
    sorted_results = sorted(results.items(), key=lambda x: float(x[1]['points']), reverse=True)
    results = {}
    for item in sorted_results:
        results[item[0]] = item[1]
    return results


def write_csv(results):
    results = sort_results(results)

    # write results in csv format
    with open(os.path.join(results_path, 'results.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Repo', 'Ping', 'Tiny files', 'Large files', 'Richness', 'Points'])
        for repo in results:
            writer.writerow([repo,
                             results[repo]['ping'],
                             results[repo]['tiny_speed'],
                             results[repo]['large_speed'],
                             results[repo]['richness'],
                             results[repo]['points']
                             ])
    return True


def gen_markdown(results):
    results = sort_results(results)

    # generate results in table format
    with open(os.path.join(results_path, 'results.md'), 'w', encoding='utf-8') as f:
        # f.write('## Results\n\n')
        header = '| Repo | Type| Ping | Tiny files | Large files | Richness | Points | Rank | Comments |\n'
        f.write('| 镜像 | 类型 | Ping | 小文件 | 大文件 | 丰富度 | 总分 | 排名 | 备注 |\n')
        # f.write('| --- ' * (header.count('|') - 1) + '|\n')
        # f.write('| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n')
        f.write('| --- | --- | --: | --: | --: | --: | --: | --- | --- |\n')
        for mirror in results:
            f.write('| [{}]({}) | {} | {} | {} | {} | {} | {} | {} | {} |\n'.format(
                all_mirrors[mirror]['name'],
                all_mirrors[mirror]['url'],
                '高校' if mirror in universities else '商业',
                results[mirror]['ping'],
                results[mirror]['tiny_speed'],
                results[mirror]['large_speed'],
                results[mirror]['richness'],
                results[mirror]['points'],  # '{:.2f}'.format(10 * float(results[mirror]['points']) ** 0.5),
                list(results.keys()).index(mirror) + 1,
                ''
            ))
    return True


if __name__ == '__main__':
    test_results = read_results(results_path)
    write_csv(test_results)
    gen_markdown(test_results)
    print('Done!')

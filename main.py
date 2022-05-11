import os
import csv
from test_mirror import test_mirror
from mirrors import universities, commercials


if __name__ == '__main__':
    results = {}
    repos = universities | commercials
    for repo in repos:
        if os.path.isfile('results/{}.txt'.format(repo)):
            print(f'Skipping {repo}')
        else:
            print('Testing {}'.format(repos[repo]['name']))
            final_points, ping_result, tiny_files_speed_str, large_files_speed_str, richness_result = test_mirror(
                repos[repo]['url'])
            results[repo] = {
                'final_points': final_points,
                'ping_result': ping_result,
                'tiny_files_speed_str': tiny_files_speed_str,
                'large_files_speed_str': large_files_speed_str,
                'richness_result': richness_result
            }
            with open('results/{}.txt'.format(repo), 'w') as f:
                f.write('Final points: {}\n'.format(final_points))
                f.write('Ping result: {}\n'.format(ping_result))
                f.write('Tiny files speed: {}\n'.format(tiny_files_speed_str))
                f.write('Large files speed: {}\n'.format(large_files_speed_str))
                f.write('Richness result: {}\n'.format(richness_result))

    with open('results/results.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Repo', 'Final points', 'Ping result', 'Tiny files speed', 'Large files speed', 'Richness result'])
        for repo in results:
            writer.writerow([
                repo,
                results[repo]['final_points'],
                results[repo]['ping_result'],
                results[repo]['tiny_files_speed_str'],
                results[repo]['large_files_speed_str'],
                results[repo]['richness_result']
            ])

    print('Done!')

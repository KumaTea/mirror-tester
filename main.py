import os
import csv
from init import initialize
from mirrors import all_mirrors
from test_mirror import test_mirror


if __name__ == '__main__':
    initialize()

    results = {}
    for mirror in all_mirrors:
        if os.path.isfile('results/{}.txt'.format(mirror)):
            print(f'Skipping {mirror}')
        else:
            print('Testing {}'.format(all_mirrors[mirror]['name']))
            final_points, ping_result, tiny_files_speed_str, large_files_speed_str, richness_result = test_mirror(
                mirror)
            results[mirror] = {
                'final_points': final_points,
                'ping_result': '{:.3f}'.format(ping_result) if ping_result != 'Failed' else ping_result,
                'tiny_files_speed_str': tiny_files_speed_str,
                'large_files_speed_str': large_files_speed_str,
                'richness_result': richness_result
            }
            with open('results/{}.txt'.format(mirror), 'w') as f:
                f.write('Final points: {}\n'.format(final_points))
                f.write('Ping result: {}\n'.format(ping_result))
                f.write('Tiny files speed: {}\n'.format(tiny_files_speed_str))
                f.write('Large files speed: {}\n'.format(large_files_speed_str))
                f.write('Richness result: {}\n'.format(richness_result))

    with open('results/results.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Repo', 'Final points', 'Ping result', 'Tiny files speed', 'Large files speed', 'Richness result'])
        for mirror in results:
            writer.writerow([
                mirror,
                results[mirror]['final_points'],
                results[mirror]['ping_result'],
                results[mirror]['tiny_files_speed_str'],
                results[mirror]['large_files_speed_str'],
                results[mirror]['richness_result']
            ])

    print('Done!')

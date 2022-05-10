from test_mirror import test_mirror
from mirrors import universities, commercials


if __name__ == '__main__':
    for repo in universities | commercials:
        print('Testing {}'.format(universities[repo]['name']))
        final_points, ping_result, tiny_files_speed_str, large_files_speed_str, richness_result = test_mirror(
            universities[repo]['url'])
        with open('results/{}.txt'.format(repo), 'w') as f:
            f.write('Final points: {}\n'.format(final_points))
            f.write('Ping result: {}\n'.format(ping_result))
            f.write('Tiny files speed: {}\n'.format(tiny_files_speed_str))
            f.write('Large files speed: {}\n'.format(large_files_speed_str))
            f.write('Richness result: {}\n'.format(richness_result))

    print('Done!')

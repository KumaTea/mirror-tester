import math
import subprocess


def ping(host, count=10, ipv='4', port=443):
    command = f'tcping -{ipv} -c {count} -p {port} {host}'
    try:
        ping_results = []
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        result_str = result.stdout.decode('utf-8')
        # Connected to www.qq.com[:80]: seq=1 time=29.60 ms
        for line in result_str.splitlines():
            if 'Connected' in line:
                time = float(line.split('time=')[1].split(' ')[0])
                ping_results.append(time)
        if not ping_results:
            # return False
            return 9999
        # remove 10% max and min
        ping_results.sort()
        ping_results = ping_results[math.ceil(count * 0.1):math.floor(count * 0.9)]
        average = sum(ping_results) / len(ping_results)
        return average
    except:
        # return False
        return 9999


def min_ping(host, count=10):
    ipv4_80_result = ping(host, count, ipv='4', port=80)
    ipv4_443_result = ping(host, count, ipv='4', port=443)
    ipv4_result = min(ipv4_80_result, ipv4_443_result)
    print(f'    IPv4: 80: {ipv4_80_result}, 443: {ipv4_443_result}')
    ipv6_80_result = ping(host, count, ipv='6', port=80)
    ipv6_443_result = ping(host, count, ipv='6', port=443)
    ipv6_result = min(ipv6_80_result, ipv6_443_result)
    print(f'    IPv6: 80: {ipv6_80_result}, 443: {ipv6_443_result}')
    if min(ipv4_result, ipv6_result) == 9999:
        return False
    else:
        return min(ipv4_result, ipv6_result)

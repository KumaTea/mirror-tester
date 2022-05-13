import subprocess


def ping(host, count=10, ipv='4'):
    command = f'ping -{ipv} -c {count} {host} | tail -n 1 | awk \'{{print $4}}\''
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    result_str = result.stdout.decode('utf-8')
    if result_str and '/' in result_str:
        # min/avg/max/mdev
        return float(result_str.split('/')[1])
    else:
        return False


def min_ping(host, count=10):
    ipv4_result = ping(host, count, ipv='4')
    print(f'    IPv4: {ipv4_result}')
    ipv6_result = ping(host, count, ipv='6')
    print(f'    IPv6: {ipv6_result}')
    if ipv4_result and ipv6_result:
        return min(ipv4_result, ipv6_result)
    else:
        return ipv4_result or ipv6_result

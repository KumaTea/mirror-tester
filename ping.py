import subprocess


def ping(host, count=10):
    command = f'ping -c {count} {host} | tail -n 1 | awk \'{{print $4}}\''
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    result_str = result.stdout.decode('utf-8')
    if result_str and '/' in result_str:
        # min/avg/max/mdev
        return float(result_str.split('/')[1])
    else:
        return False

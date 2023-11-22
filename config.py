# Result rates
rates = {
        'ping': 10,
        'tiny': 48,
        'large': 36,
        'rich': 6
}

# Timeouts
avail_test_timeout = 5
tiny_test_timeout = 5
large_test_timeout = 120

# Samples
repo_samples = 5
tiny_files_samples = 100
large_files_samples = 5

# Max speed
tiny_max_speed = 1000 * 1024  # 1000 KB/s
large_max_speed = 100 * 1024 * 1024  # 100 MB/s

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

size_dict = {
    # power of 1024
    'KiB': 1,
    'MiB': 2,
    'GiB': 3,
    'TiB': 4,
    'PiB': 5,
    'EiB': 6,
    'ZiB': 7,
    'YiB': 8,
}


def get_file_size_unit(bytes_count):
    assert type(bytes_count) in (int, float)
    if bytes_count < 1024:
        return bytes_count, "B"
    else:
        for size_name, size_power in size_dict.items():
            if bytes_count < 1024 ** (size_power + 1):
                return bytes_count / 1024 ** size_power, size_name
        return bytes_count, "B"

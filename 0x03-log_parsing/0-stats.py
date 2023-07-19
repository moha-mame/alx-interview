#!/usr/bin/python3

import sys


def print_statistics(status_codes, total_file_size):
    """
    Print statistics for status codes and total file size.
    Args:
        status_codes (dict): Dictionary containing status code counts.
        total_file_size (int): Total file size.
    Returns:
        None
    """
    print("File size:", total_file_size)
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print(f"{code}: {count}")


def main():
    total_file_size = 0
    counter = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            parsed_line = line.split()[::-1]  # Split and reverse the line

            if len(parsed_line) > 2:
                counter += 1

                if counter <= 10:
                    total_file_size += int(parsed_line[0])  # file size
                    code = parsed_line[1]  # status code

                    if (code in status_codes.keys()):
                        status_codes[code] += 1

                if counter == 10:
                    print_statistics(status_codes, total_file_size)
                    counter = 0
    finally:
        print_statistics(status_codes, total_file_size)

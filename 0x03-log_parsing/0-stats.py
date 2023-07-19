#!/usr/bin/python3
import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {}


def print_statistics():
    '''Extracts sections of a line of an HTTP request log.
    '''
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")


def signal_handler(sig, frame):
    '''A script for
    '''
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line_number, line in enumerate(sys.stdin, 1):
        try:
            ip, _, _, _, _, status_code_str, file_size_str = line.strip().split()[0:7]
            status_code = int(status_code_str)
            file_size = int(file_size_str)
        except (ValueError, IndexError):
            continue

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        # Print statistics after every 10 lines
        if line_number % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    pass

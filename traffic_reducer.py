#!/usr/bin/env python3
import sys

def main():
    current_key = None
    running_sum = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        fields = line.split("\t")
        if len(fields) < 3:
            continue

        boro = fields[0]
        date_part = fields[1]
        try:
            vol = int(fields[2])
        except ValueError:
            continue

        key = (boro, date_part)

        if current_key and key != current_key:
            print(f"{current_key[0]}\t{current_key[1]}\t{running_sum}")
            running_sum = 0

        current_key = key
        running_sum += vol

    if current_key:
        print(f"{current_key[0]}\t{current_key[1]}\t{running_sum}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        # Skip header if it starts with request_id or is empty
        if line.startswith("request_id") or not line:
            continue

        fields = line.split(",")
        if len(fields) < 9:
            continue

        boro = fields[1]
        vol_str = fields[7]
        dt_str = fields[8]  # "YYYY-MM-DD HH:MM"

        try:
            vol = int(vol_str)
        except ValueError:
            continue

        date_part = dt_str.split(" ")[0]  # "YYYY-MM-DD"
        print(f"{boro}\t{date_part}\t{vol}")

if __name__ == "__main__":
    main()

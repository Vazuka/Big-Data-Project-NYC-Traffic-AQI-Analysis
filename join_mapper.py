#!/usr/bin/env python3
import sys
import os

def main():
    input_file = os.environ.get("mapreduce_map_input_file", "")
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Decide if it's a traffic summary or air quality line
        if "traffic_output_groupby" in input_file or "traffic_summary.txt" in input_file:
            fields = line.split("\t")
            if len(fields) < 3:
                continue
            boro = fields[0]
            date_part = fields[1]
            total_vol = fields[2]
            
            print(f"{boro}\t{date_part}\tT|{total_vol}")
        
        elif "air_quality" in input_file:
            fields = line.split(",")
            if len(fields) < 4:
                continue
            
            geo_place = fields[1].strip()
            start_date = fields[2].strip()
            data_val = fields[3].strip()
            
            print(f"{geo_place}\t{start_date}\tA|{data_val}")
        else:
            pass

if __name__ == "__main__":
    main()

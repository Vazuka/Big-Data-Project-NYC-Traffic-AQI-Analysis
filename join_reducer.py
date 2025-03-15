#!/usr/bin/env python3
import sys

def main():
    current_key = None
    traffic_list = []
    aq_list = []
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        fields = line.split("\t")
        if len(fields) < 3:
            continue
        
        boro_or_place = fields[0]
        date_part = fields[1]
        
        tagged_value = fields[2]
        
        key = (boro_or_place, date_part)
        
        # If encountered a new key, process old key first
        if current_key and key != current_key:
            for tv in traffic_list:
                for av in aq_list:
                    print(f"{current_key[0]}\t{current_key[1]}\t{tv}\t{av}")
            
            # Reset lists
            traffic_list = []
            aq_list = []
        
        current_key = key
        
        parts = tagged_value.split("|", 1)
        record_type = parts[0]
        record_val = parts[1] if len(parts) > 1 else ""
        
        if record_type == "T":
            traffic_list.append(record_val)
        elif record_type == "A":
            aq_list.append(record_val)
    
    if current_key:
        for tv in traffic_list:
            for av in aq_list:
                print(f"{current_key[0]}\t{current_key[1]}\t{tv}\t{av}")

if __name__ == "__main__":
    main()

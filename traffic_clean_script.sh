#!/usr/bin/env bash

INPUT_FILE="NYC_Traffic_Volume_Counts.csv"
OUTPUT_FILE="clean_traffic_data.csv"

awk -F',' 'BEGIN {OFS=","}
NR==1 {
   print $0,"date_time"
}
NR>1 {
   if($3 != "" && $4 != "" && $5 != "" && $8 != ""){
     dt = $3 "-" sprintf("%02d",$4) "-" sprintf("%02d",$5) " " \
          sprintf("%02d",$6) ":" sprintf("%02d",$7)
     print $0, dt
   }
}' "$INPUT_FILE" > "$OUTPUT_FILE"

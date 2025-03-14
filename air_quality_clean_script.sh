#!/usr/bin/env bash

INPUT_AQ="NYC_air_quality.csv"
OUTPUT_AQ="air_quality_cleaned.csv"

awk -F',' 'BEGIN {OFS=","}
NR==1 {
   print $0
}
NR>1 {
   if($10 != "" && $11 != ""){
     split($10, d, "/")
     newDate = d[3] "-" sprintf("%02d",d[1]) "-" sprintf("%02d",d[2])
     $10 = newDate
     print $0
   }
}' "$INPUT_AQ" > "$OUTPUT_AQ"

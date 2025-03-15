#!/usr/bin/env bash

MYSQL_USER="root"
MYSQL_PASS="Nikhilmysql23"
DB_NAME="nyc_data"
TRAFFIC_CSV="clean_traffic_data.csv"

mysql --local-infile=1 -u "$MYSQL_USER" -p"$MYSQL_PASS" -e "
USE $DB_NAME;
LOAD DATA LOCAL INFILE '$TRAFFIC_CSV'
INTO TABLE traffic_data
FIELDS TERMINATED BY ','
IGNORE 1 LINES
(request_id,
 boro,
 year,
 month,
 day,
 hour,
 minute,
 vol,
 @dummy1, @dummy2, @dummy3, @dummy4, @dummy5,
 date_time
);
"

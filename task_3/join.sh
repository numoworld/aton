#!/bin/bash

file_1=$(sed "1d" file_1.csv | sort -k 3 -t ';' | awk -F ";" '{print $2 ";" $3}')
file_2=$(sed "1d" file_2.csv | sort -k 2 -t ';' | awk -F ";" '{print $2 ";" $3}')

echo 'No;ip;groupname;member' > result.csv
join -t ';' -1 2 -2 1 -o 1.1,1.2,2.2 <(echo "$file_1") <(echo "$file_2") | awk '{printf "%s;%s\n", NR,$0}' >> result.csv
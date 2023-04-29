#! /usr/bin/bash

echo -e "enter directory in which to search for .csv files:"

read directory

find "$directory" -type f -name "*.csv" -exec basename {} .csv ';'
#!/bin/bash
echo "Enmiao's Data processing"
DATE=`date +%Y-%m-%d`
echo "Date is: "$DATE
echo "The name of the file is: ds_salaries.csv"
lines=$(wc -l < ds_salaries.csv)
echo "The file has" $lines "lines"
colnames=$(head -n 1 < ds_salaries.csv)
echo "Column names are: "
echo $colnames
echo "List of items in the descending order of salaries:"
sorted=$(sort -k6 -n -r -t, ds_salaries.csv)
echo $sorted
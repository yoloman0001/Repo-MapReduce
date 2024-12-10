#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

highest_sales = {} # this dictionary uses payment as the key and stores cost

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        if payment not in highest_sales or cost > highest_sales[payment]:
            highest_sales[payment] = cost

for payment, cost in highest_sales.items():
    print(payment+"\t"+cost)

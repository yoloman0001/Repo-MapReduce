#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

max_sale = 0.0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        cost = float(cost) # cost is a str, to get the absolute value first we need to convert it to a number
        if cost > max_sale:
            max_sale = abs(cost)

print(max_sale)

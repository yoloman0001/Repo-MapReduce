#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

# Exercicio 1.1
# Mellora o codigo de xeito que se encontra algunha linha
# cun formato non axeitado a descarte e siga traballando coa linha seguinte
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print(store+"\t"+cost)

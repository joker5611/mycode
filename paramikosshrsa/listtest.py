#!/usr/bin python3

import csv

def main():
    with open('confile.txt', 'r') as confile:
        condata = csv.reader(confile, delimiter=",")
        for row in condata:
            print(row[0][1])

main()

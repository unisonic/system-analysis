import csv
import sys

data = sys.argv[1]
row = int(sys.argv[2])
column = int(sys.argv[3])

with open(data, newline='') as csvfile:
    csv_table = list(csv.reader(csvfile, delimiter=','))
    print(csv_table[row - 1][column - 1])

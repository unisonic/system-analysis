import csv
import sys
import math


def task(csv_rows):
    n = len(csv_rows)
    
    ans = 0.0
    for vertex, row in enumerate(csv_rows):
        for relation in row:
            if int(relation) == 0:
                continue

            fraction = int(relation) / (n - 1)
            ans -= fraction * math.log2(fraction)
    
    return round(ans, 1)


if __name__ == "__main__":
    with open(sys.argv[1], newline='') as csvfile:
        print(task(list(csv.reader(csvfile, delimiter=','))))

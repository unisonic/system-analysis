import csv
import sys
import math

data = sys.argv[1]
with open(data, newline='') as csvfile:
    csv_rows = list(csv.reader(csvfile, delimiter=','))
    n = len(csv_rows)
    
    ans = 0.0
    for vertex, row in enumerate(csv_rows):
        for relation in row:
            if int(relation) == 0:
                continue

            fraction = int(relation) / (n - 1)
            ans -= fraction * math.log2(fraction)
    
    print(round(ans, 1))



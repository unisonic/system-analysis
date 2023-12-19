import json
import math
import sys


def read_json(file):
    with open(file, 'r') as jsonfile:
        result = json.load(jsonfile)
    return result

def get_object_count(exp):
    result = 0
    for obj in exp:
        if isinstance(obj, int):
            result += 1
        else:
            result += len(obj)
    return result


exp = [read_json(sys.argv[i]) for i in range(1, len(sys.argv))]
n = len(exp[0])
m = len(exp)

x = [0] * n
for obj in range(n):
    for dude in range(m):
        x[obj] += exp[dude][obj]

X = sum(x) / n
S = sum(map(lambda Xi: (Xi - X) ** 2, x))

print(round(12 * S / m / m / (n ** 3 - n), 2))

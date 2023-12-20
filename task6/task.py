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

def task(expA, expB):
    exp = [expA, expB]
    n = len(expA)
    m = 2

    x = [0] * n
    for obj in range(n):
        for dude in range(m):
            x[obj] += exp[dude][obj]

    X = sum(x) / n
    S = sum(map(lambda Xi: (Xi - X) ** 2, x))

    return round(12 * S / m / m / (n ** 3 - n), 2)


if __name__ == "__main__":
    expA = read_json(sys.argv[1])
    expB = read_json(sys.argv[2])
    print(task(expA, expB))

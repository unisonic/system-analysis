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
    

def calculate_positions(n, exp):
    result = [0 for i in range(n + 1)]
    
    k = 1
    for obj in exp:
        if isinstance(obj, int):
            result[obj] = k
        else:
            for nested in obj:
                result[nested] = k
        k += 1

    return result


posA, posB = [], []
def contradict(x, y):
    if x > aN or x > bN or y > aN or y > bN:
        return False
    if (posA[x] - posA[y]) * (posB[x] - posB[y]) < 0:
        return True
    return False
def both_equal(x, y):
    if x <= aN and y <= aN and posA[x] != posA[y]:
        return False
    if x <= bN and y <= bN and posB[x] != posB[y]:
        return False
    return True


aN, bN = 0, 0
snm, group = [], []
def unite(x, y):
    gx = group[x]
    gy = group[y]
    if gx == gy:
        return

    if len(snm[gx]) > len(snm[gy]):
        for elem in snm[gy]:
            group[elem] = gx
            snm[gx].extend(snm[gy])
            snm[gy].clear()
    else:
        for elem in snm[gx]:
            group[elem] = gy
            snm[gy].extend(snm[gx])
            snm[gx].clear()


def less(x, y):
    if group[x] == group[y]:
        return False
    if x <= aN and y <= bN and posA[x] < posA[y]:
        return True
    if x <= bN and y <= bN and posB[x] < posB[y]:
        return True
    return False


def task(expA, expB):
    global aN, bN, snm, group, posA, posB
    aN = get_object_count(expA)
    bN = get_object_count(expB)

    posA = calculate_positions(aN, expA)
    posB = calculate_positions(bN, expB)

    snm = [[i] for i in range(max(aN, bN) + 1)]
    group = [i for i in range(max(aN, bN) + 1)]

    for i in range(1, max(aN, bN) + 1):
        for j in range(1, max(aN, bN) + 1):
            if i == j:
                continue
            if contradict(i, j) or both_equal(i, j): 
                unite(i, j)

    order = [i + 1 for i in range(max(aN, bN))]
    for i in range(len(order)):
        for j in range(len(order) - 1):
            if less(order[j + 1], order[j]):
                order[j], order[j + 1] = order[j + 1], order[j]


    result = []
    used = [0 for i in range(max(aN, bN) + 1)]
    for i in order:
        if used[i] == 1:
            continue
        
        gi = group[i]
        if len(snm[gi]) > 1:
            for elem in snm[gi]:
                used[elem] = 1
            result.append(snm[gi])
        else:
            used[i] = 1
            result.append(i)

    return result


if __name__ == "__main__":
    expA = read_json(sys.argv[1])
    expB = read_json(sys.argv[2])
    print(task(expA, expB))

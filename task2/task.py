import csv
import sys

data = sys.argv[1]

max_vertex = 0
edges = {}

with open(data, newline='') as csvfile:
    csv_rows = list(csv.reader(csvfile, delimiter=','))
    for row in csv_rows:
        a, b = [int(i) for i in row]
        max_vertex = max(max_vertex, a, b)
        if a not in edges:
            edges[a] = [b]
        else:
            edges[a].append(b)

used = [0 for i in range(max_vertex + 1)]
answer = [[0 for i in range(5)] for j in range(max_vertex + 1)]

def dfs(v):
    used[v] = 1
    if v not in edges:
        return
    
    answer[v][0] = len(edges[v])
    for to in edges[v]:
        answer[to][1] += 1
        answer[to][4] += answer[v][0] - 1
        if to in edges:
            answer[v][2] += len(edges[to])
            for goto in edges[to]:
                answer[goto][3] = 1

        if used[to] == 0:
            dfs(to)

for i in range(1, max_vertex + 1):
    if (i not in edges) or used[i] == 1:
        continue
    dfs(i)

with open('answer.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for i in range(1, max_vertex + 1):
        writer.writerow(answer[i])

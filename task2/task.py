import csv
import sys


used = []
edges = {}
answer = []
max_vertex = 0


def dfs(v):
    global used, edges, answer

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


def task(csv_rows):
    global max_vertex, used, edges, answer

    for row in csv_rows:
        a, b = [int(i) for i in row]
        max_vertex = max(max_vertex, a, b)
        if a not in edges:
            edges[a] = [b]
        else:
            edges[a].append(b)
    
    used = [0 for i in range(max_vertex + 1)]
    answer = [[0 for i in range(5)] for j in range(max_vertex + 1)]
    for i in range(1, max_vertex + 1):
        if (i not in edges) or used[i] == 1:
            continue
        dfs(i)


if __name__ == "__main__":
    with open(sys.argv[1], newline='') as csvfile:
        task(list(csv.reader(csvfile, delimiter=',')))
    with open('answer.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for i in range(1, max_vertex + 1):
            writer.writerow(answer[i])

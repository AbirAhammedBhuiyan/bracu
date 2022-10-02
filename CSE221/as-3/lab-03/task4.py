#!/usr/bin/env python3


# ==============================
# Title: CSE221 lab-03 task-04
# Author: Abir Ahammed Bhuiyan
# ID: 20101197
# ==============================


def optimalBFS(graph, start):

    visited = [False]*len(graph)
    queue = []
    bridgeCrossed = [0]*len(graph)

    visited[int(start)-1] = True
    queue.append(start)

    while len(queue) != 0:

        node = queue.pop(0)

        for neighbour in graph[node]:
            if visited[int(neighbour)-1] == False:
                visited[int(neighbour)-1] = True
                queue.append(neighbour)
                bridgeCrossed[int(neighbour)-1] += bridgeCrossed[int(node)-1] + 1

    return bridgeCrossed


def createBidirGraph(filePointer, edges):

    graph = {}

    for edge in range(edges):
        come, go = list(filePointer.readline().split())

        if graph.get(come):
            graph[come].append(go)
        else:
            graph[come] = []
            graph[come].append(go)

        if graph.get(go):
            graph[go].append(come)
        else:
            graph[go] = []
            graph[go].append(come)

    return graph



if __name__ == "__main__":

    output = ""

    with open('input4.txt', 'r') as fr:
        t = int(fr.readline())

        while t:
            n, m = list(map(int, fr.readline().split()))
            graph = createBidirGraph(fr,  m)
            bridgeCrossed = optimalBFS(graph, '1')
            output += f"{bridgeCrossed[n-1]}\n"
            t -= 1

    with open('output4.txt', 'w') as fw:
        fw.write(output)



    





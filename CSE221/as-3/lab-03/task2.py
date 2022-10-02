#!/usr/bin/env python3


# ==============================
# Title: CSE221 lab-03 task-02
# Author: Abir Ahammed Bhuiyan
# ID: 20101197
# ==============================


import task1


def BFS(graph, node, endPoint):

    path = ""

    visited = [False]*len(graph)
    queue = []

    visited[int(node)-1] = True
    queue.append(node)

    while len(queue) != 0:
        m = queue.pop(0)

        path += m + " "

        if m == endPoint:
            break
        
        for neighbour in graph[m]:

            if visited[int(neighbour)-1] == False:
                visited[int(neighbour)-1] = True
                queue.append(neighbour)

    return path[:-1]



if __name__ == "__main__":

    graph = task1.createGraph('input1.txt')
    path = BFS(graph, '1', '12')

    with open('output2.txt', 'w') as fw:
        fw.write(f"Places: {path}\n")




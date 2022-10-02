#!/usr/bin/env python3


# ==============================
# Title: CSE221 lab-03 task-03
# Author: Abir Ahammed Bhuiyan
# ID: 20101197
# ==============================


import task1


def DFS_VISIT(graph, node):
    visited[int(node)-1] = True
    mainPath.append(node)

    for neighbour in graph[node]:
        if visited[int(neighbour)-1] == False:
            DFS_VISIT(graph, neighbour)


def DFS(graph, endPoint):

    path = ""

    for node in graph:
        if visited[int(node)-1] == False:
            DFS_VISIT(graph, node)

    for node in mainPath:

        if node == endPoint:
            path += node
            break

        path += node + " "

    return path



if __name__ == "__main__":

    graph = task1.createGraph('input1.txt')

    visited = [False]*len(graph)

    mainPath = []

    path = DFS(graph, '12')

    with open('output3.txt', 'w') as fw:
        fw.write(f"Places: {path}\n")
    

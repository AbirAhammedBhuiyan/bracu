#!/usr/bin/env python3


# ==============================
# Title: CSE221 lab-03 task-01
# Author: Abir Ahammed Bhuiyan
# ID: 20101197
# ==============================


# def sortGraph(graph):
#     sorted_keys = sorted(list(graph.keys()), key = lambda x: int(x))
#     return {k : graph[k] for k in sorted_keys}


def createGraph(fileName):

    graph = {}

    with open('./'+fileName, 'r') as fr:
        total_places = int(fr.readline())
        total_edges = int(fr.readline())

        for edge in range(total_edges):
            come, go = list(fr.readline().split())

            if graph.get(come):
                graph[come].append(go)
            else:
                graph[come] = []
                graph[come].append(go)

        # checking for a child node that is empty and doesn't exist
        # and giving it a list
            if graph.get(go) == None:
                graph[go] = []

    return graph



def printGraph(fileName, graph):

    with open('./'+fileName, 'w') as fw:
        for key, value in graph.items():
            fw.write(str(key))

            for elem in graph[key]:
                fw.write('\t' + str(elem))

            fw.write('\n')




if __name__ == "__main__":

    graph = createGraph('input1.txt')

    printGraph('output1.txt', graph)


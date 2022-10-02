#!/usr/bin/env python3

from pprint import pprint
from heapq import heappush, heappop, show_tree
import sys


'''
Implementation of "Dijsktra's algo"

@param {dict} -> graph as adjacency list
@param {src} -> source, basically where it should start traversing
@returns {dict} -> minimum cost to reach each vertex from source
'''

def dijsktra(graph, src):

    dist = {}
    dist[src] = 0
    q = []
    visited = {}

    for v in graph.keys():
        if v != src: 
            dist[v] = sys.maxsize

        heappush(q, (dist[v], v))
        visited[v] = False


    while q:
        u = heappop(q)[1]

        if visited[u]:
            continue

        visited[u] = True

        for neighbour in graph[u]:
            alt = dist[u] + graph[u][neighbour]

            if alt < dist[neighbour]:
                dist[neighbour] = alt

                heappush(q, (dist[neighbour], neighbour))

    return dist


'''
 Makes undirected graph using 'adjacency list'.

 @param {io.TextIOWrapper} -> file pointer to navigate through the file 
 @returns {tuple} (str, dict) -> str: destination vertex | dict: the graph
 '''

def graphMaker(fr):

    vertices, edges = list(map(int, fr.readline().split()))

    if edges == 0:
        return ( str(vertices), { '1': {} } )

    graph = {}

    for edge in range(edges):
        come, go, weight = fr.readline().split()

        if graph.get(come):
            graph[come][go] = int(weight)
        else:
            graph[come] = {}
            graph[come][go] = int(weight)

        if graph.get(go):
            graph[go][come] = int(weight)
        else:
            graph[go] = {}
            graph[go][come] = int(weight)

    return ( str(vertices), graph )



if __name__ == "__main__":

    result = ""

    with open("./input1.txt", "r") as fr:

        t = int(fr.readline())

        while t:

            dest, graph = graphMaker(fr)
            dist = dijsktra(graph, '1')
            result += str(dist[dest]) + "\n"

            t -= 1


    with open("./output1.txt", "w") as fw:

        fw.write(result)


#!/usr/bin/env python3

from pprint import pprint
from heapq import heappush, heappop
from formatter import stringify         # custom module for printing list
import sys


'''
Implementation of "Dijsktra's algo"

@param {dict} -> graph as adjacency list
@param {str} -> source, basically where it should start traversing
@returns {tuple} (dict, dict) -> dict: minimum cost to reach each vertex from source
                                 dict: previously reached vertex while finding the shortest path
'''

def dijsktra(graph, src):

    dist = {}
    visited = {}
    prev = {}
    dist[src] = 0
    q = []

    for v in graph.keys():
        if v != src: 
            dist[v] = sys.maxsize
            prev[v] = None

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
                prev[neighbour] = u

                heappush(q, (dist[neighbour], neighbour))

    return ( dist, prev )



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



'''
Backtracing and building the shortest path from source to destination

@param {dict} -> previously reached vertex while finding the shortest path
@param {str} -> source vertex
@param {dest} -> destination vertex
@returns {list} -> constructed shortest path from source to destination
'''

def pathBuilder(prev, src, dest):
    if len(prev) == 0:
        return src

    pointer = dest

    path = []

    while pointer != src: 
        path.append(pointer)
        pointer = prev[pointer]
    path.append(src)

    return path[::-1]



if __name__ == "__main__":

    result = ""

    with open("./input1.txt", "r") as fr:

        t = int(fr.readline())

        while t:

            dest, graph = graphMaker(fr)
            dist, prev = dijsktra(graph, '1')
            path = pathBuilder(prev, '1', dest)
            result += stringify(path) + "\n"

            t -= 1

    with open("./output2.txt", "w") as fw:
        fw.write(result)


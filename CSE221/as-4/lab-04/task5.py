#!/usr/bin/env python3

from pprint import pprint
from heapq import heappush, heappop
from formatter import stringify         # custom module for printing list
import sys


'''
implmentation of the pseudocode using "Dijkstra's algo" knowledge

@param {dict} -> graph as adjacency list
@param {str} -> source, basically where it should start traversing
@returns {dic} -> cost (maximum data transfer rate) from source to each vertex
'''

def Network(graph, src):

    dist = {}
    dist[src] = sys.maxsize
    q = []

    for v in graph.keys():
        if v != src: 
            dist[v] = (-1)*sys.maxsize

        heappush(q, (dist[v], v))

    while q:
        u = heappop(q)[1]

        for neighbour in graph[u]:
            alt = min(dist[u], graph[u][neighbour])

            if alt > dist[neighbour]:
                dist[neighbour] = alt

                heappush(q, (dist[neighbour], neighbour))

    for key, value in dist.items():
        if value == (-1)*sys.maxsize:
            dist[key] = -1
    
    dist[src] = 0

    return dist



'''
 Makes directed graph using 'adjacency list'.

 @param {io.TextIOWrapper} -> file pointer to navigate through the file 
 @returns {tuple} (str, dict) -> str: source vertex | dict: the graph
 '''

def graphMaker(fr):

    vertices, edges = list(map(int, fr.readline().split()))

    if edges == 0:
        src = fr.readline().split()[0]
        return ( src, { '1': {} } )

    graph = {}

    for edge in range(edges):
        come, go, weight = fr.readline().split()

        if graph.get(come):
            graph[come][go] = int(weight)
        else:
            graph[come] = {}
            graph[come][go] = int(weight)

        if graph.get(go) == None:
            graph[go] = {}

    src = fr.readline().split()[0]

    return ( src, graph )



'''
Sorting the dictionary in ascending order using keys &
constructing a printable format of the value(s)

@param {dict} -> cost(s) (maximum data transfer rate)
@returns {str} -> constructed string for printing
'''

def dicToPrintFormat(dist):

    sil = []

    sorted_keys = sorted(list(dist.keys()), key = lambda x: int(x))
    dist = {k : dist[k] for k in sorted_keys}

    for key, value in dist.items():
        sil.append(value)

    return stringify(sil)



if __name__ == "__main__":

    result = ""

    with open("./input5.txt", "r") as fr:

        t = int(fr.readline())

        while t:

            src, graph = graphMaker(fr)
            dist = Network(graph, src)
            result += dicToPrintFormat(dist) + "\n"

            t -= 1

    with open("./output5.txt", "w") as fw:
        fw.write(result)




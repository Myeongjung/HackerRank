#!/bin/python3

import math
import os
import random
import re
import sys

def DFS(adj,s,visited,val):
    visited[s] = 1
    val += 1
    for i in adj[s]:
        if visited[i]==0:
            val = DFS(adj,i,visited,val)

    return val

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road>c_lib:
        return n*c_lib

    adj = {}
    for i in cities:
        if i[0] in adj:
            adj[i[0]].append(i[1])
        else:
            adj[i[0]] = [i[1]]

        if i[1] in adj:
            adj[i[1]].append(i[0])
        else:
            adj[i[1]] = [i[0]]

    for i in range(1, n+1):
        if i in adj:
            pass
        else:
            adj[i] = []

    visited = [0]*(n+1)

    countNodes = 0
    countComponents = 0

    l = []
    for i in range(1,n+1):
        if visited[i]==0:
            val = 0
            nodes = DFS(adj,i,visited,val)
            countComponents += 1
            l.append(nodes)

    total = 0
    for i in l:
        total = total + (c_road*(i-1))

    total = total + countComponents*c_lib

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
 
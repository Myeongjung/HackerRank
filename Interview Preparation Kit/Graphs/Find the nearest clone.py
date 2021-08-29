from queue import Queue

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    g = {i + 1: [] for i in range(graph_nodes)}
    for i in range(len(graph_from)):
        g[graph_from[i]].append(graph_to[i])
        g[graph_to[i]].append(graph_from[i])

    target_nodes = []

    for i in range(len(ids)):
        if ids[i] == val:
            target_nodes.append(i + 1)
    result = -1
    for node in target_nodes:
        w = weight(g, target_nodes, node, result)
        if w >0 and w < result or result == -1:
            result = w
    return result

def weight(g, target_nodes, node, limit=-1):
    visited = set()
    q = Queue()
    q.put((node, 0))
    while not q.empty():
        n, w = q.get()
        if n in visited:
            continue
        if n in target_nodes and n != node:
            return w
        visited.add(n)
        if w == limit:
            return -1
        for next_node in g[n]:
            if next_node not in visited:
                q.put((next_node, w + 1))
    return -1
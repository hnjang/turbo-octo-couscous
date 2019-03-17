#!/usr/bin/python3

from pprint import pprint


def connected_components(neighbors):
    seen = set()

    def component(node):
        nodes = set([node])
        while nodes:
            node = nodes.pop()
            seen.add(node)
            nodes |= neighbors[node] - seen
            yield node

    for node in neighbors:
        if node not in seen:
            yield component(node)


def solution(n, coms):
    g = dict()
    for i, row in enumerate(coms):
        g[i] = []
        for j, c in enumerate(row):
            if c: g[i].append(j)
    # pprint(g.adj)
    cc = connected_components(g)
    l_cc = list(cc)
    for e in l_cc:
        pprint(e)
    return len(l_cc)


# Driver Code
if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

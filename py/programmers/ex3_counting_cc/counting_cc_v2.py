#!/usr/bin/python3

from pprint import pprint


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [set() for i in range(V)]
        self.active_vertex = [False for i in range(V)]
        self.clear_visited()

    def clear_visited(self):
        self.visited = [False for i in range(self.V)]

    def get_vertex_stat(self, v):
        return self.active_vertex[v]

    def set_vertex_stat(self, v, val):
        self.active_vertex[v] = val

    def component(self, v):
        self.visited[v] = True
        result = [v]

        for i in self.adj[v]:
            if self.visited[i] == False:
                # Update the list
                result.extend(self.component(i))
        return result

    def addEdge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)

    def connectedComponents(self):
        cc = []
        self.clear_visited()
        for v in range(self.V):
            if self.visited[v] == False and self.get_vertex_stat(v):
                cc.append(self.component(v))
        return cc


def solution(image):
    r = len(image)
    c = len(image[0])
    img = [[0] + i + [0] for i in image]
    img.append([0] * (c + 2))
    img.insert(0, [0] * (c + 2))
    # pprint(img)
    g = Graph(r * c)
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if 0 == img[i][j]:
                continue
            curr = (i - 1) * c + (j - 1)
            g.set_vertex_stat(curr, True)
            if img[i][j + 1]: g.addEdge(curr, curr + 1)
            if img[i + 1][j]: g.addEdge(curr, curr + c)
            if img[i - 1][j]: g.addEdge(curr, curr - c)
    # pprint(g.adj)
    cc1 = g.connectedComponents()
    #pprint(cc1)
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if 0 == img[i][j]:
                continue
            curr = (i - 1) * c + (j - 1)
            g.set_vertex_stat(curr, True)
            if img[i + 1][j + 1]: g.addEdge(curr, curr + c + 1)
            if img[i + 1][j - 1]: g.addEdge(curr, curr + c - 1)
    # pprint(g.adj)
    cc2 = g.connectedComponents()
    return [len(cc1), len(cc2)]


def check_result(actual, expected):
    return (actual, expected, actual == expected)


# Driver Code
if __name__ == "__main__":
    print(
        solution([[1, 1, 0, 1, 1], [0, 1, 0, 1, 1], [1, 0, 0, 0, 1],
                  [1, 1, 0, 1, 0]]))
    print(
        solution([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1],
                  [1, 0, 0, 0]]))

    print('TC 1: actual: {}, expected: {}, result: {}'.format(*check_result(
        solution([[1, 1, 0, 1, 1], [0, 1, 0, 1, 1], [1, 0, 0, 0, 1],
                  [1, 1, 0, 1, 0]]), [4, 2])))
    print('TC 2: actual: {}, expected: {}, result: {}'.format(*check_result(
        solution([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1],
                  [1, 0, 0, 0]]), [3, 2])))

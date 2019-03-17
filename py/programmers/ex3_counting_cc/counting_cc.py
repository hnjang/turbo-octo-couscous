#!/usr/bin/python3

from pprint import pprint


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [set() for i in range(V)]
        self.active_vertex = [False for i in range(V)]

    def is_active(self, v):
        return self.active_vertex[v]

    def component(self, temp, v, visited):

        visited[v] = True

        temp.append(v)

        for i in self.adj[v]:
            if visited[i] == False:
                # Update the list
                temp = self.component(temp, i, visited)
        return temp

    def addEdge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False and self.is_active(v):
                temp = []
                cc.append(self.component(temp, v, visited))
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
            g.active_vertex[curr] = True
            if img[i][j + 1]: g.addEdge(curr, curr + 1)
            if img[i][j - 1]: g.addEdge(curr, curr - 1)
            if img[i + 1][j]: g.addEdge(curr, curr + c)
            if img[i - 1][j]: g.addEdge(curr, curr - c)
    # pprint(g.adj)
    cc1 = g.connectedComponents()
    #pprint(cc1)
    g = Graph(r * c)
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if 0 == img[i][j]:
                continue
            curr = (i - 1) * c + (j - 1)
            g.active_vertex[curr] = True
            if img[i][j + 1]: g.addEdge(curr, curr + 1)
            if img[i + 1][j]: g.addEdge(curr, curr + c)
            if img[i - 1][j]: g.addEdge(curr, curr - c)
            if img[i + 1][j + 1]: g.addEdge(curr, curr + c + 1)
            if img[i + 1][j - 1]: g.addEdge(curr, curr + c - 1)
    # pprint(g.adj)
    cc2 = g.connectedComponents()
    return [len(cc1), len(cc2)]


# Driver Code
if __name__ == "__main__":
    print(
        solution([[1, 1, 0, 1, 1], [0, 1, 0, 1, 1], [1, 0, 0, 0, 1],
                  [1, 1, 0, 1, 0]]))
    print(
        solution([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1],
                  [1, 0, 0, 0]]))

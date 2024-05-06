class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        selected = [False] * self.V
        min_edge = [float('inf')] * self.V
        min_edge[0] = 0
        parent = [-1] * self.V
        mst_cost = 0

        for _ in range(self.V):
            min_vertex = -1
            for v in range(self.V):
                if not selected[v] and (min_vertex == -1 or min_edge[v] < min_edge[min_vertex]):
                    min_vertex = v

            selected[min_vertex] = True
            mst_cost += min_edge[min_vertex]

            for v, w in self.graph[min_vertex]:
                if not selected[v] and w < min_edge[v]:
                    min_edge[v] = w
                    parent[v] = min_vertex

        print("Edges in the constructed MST:")
        for v in range(1, self.V):
            print(parent[v], "--", v, "==", min_edge[v])
        print("Minimum Spanning Tree Cost:", mst_cost)


# Example Usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim_mst()

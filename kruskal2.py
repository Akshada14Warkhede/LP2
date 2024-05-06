class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    def kruskal_mst(self):
        parent = list(range(self.V))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        result = []
        total_cost = 0
        for w, u, v in sorted(self.graph):
            if find(u) != find(v):
                result.append((u, v, w))
                total_cost += w
                parent[find(u)] = find(v)
        print("Edges in the constructed MST:")
        for u, v, w in result:
            print("%d -- %d == %d" % (u, v, w))
        print("Minimum Spanning Tree Cost:", total_cost)

# Example Usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.kruskal_mst()

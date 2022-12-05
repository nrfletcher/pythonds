""" The graph data structure is a more generalized form of a tree, or we can say that a tree is a specific type
    of graph

    Graphs can be formally defined as G = (V, E) where V is a set of vertices and E is a set of edges which can be
    defined as a list of tuples (v, w) that have two nodes (vertices) representing a connection. Edges can optionally
    have weights as well

    Graph can have direction to them if edges go a certain direction, and if this directed connection leads a node
    back to itself, it is a directed cyclic graph. If a graph has directed edges, but they do not return, the
    graph is a directed acyclic graph, or DAG """


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.vertices_count = 0

    def add_vertex(self, key):
        self.vertices_count += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertices

    def add_edge(self, f, t, weight=0):
        if f not in self.vertices:
            nv = self.add_vertex(f)
        if t not in self.vertices:
            nv = self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

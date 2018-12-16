class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def get_neighbors(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def get_vertex(self, node):
        if node in self.vertices:
            return self.vertices[node]
        else:
            return None

    def add_edge(self, start_node, final_node, weight=1):
        if start_node not in self.vertices:
            self.add_vertex(start_node)
        if final_node not in self.vertices:
            self.add_vertex(final_node)

        self.vertices[start_node].add_neighbor(self.vertices[final_node], weight)
        self.vertices[final_node].add_neighbor(self.vertices[start_node], weight)

    def get_vertices(self):
        return self.vertices.keys()

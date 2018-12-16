from searchType import SearchType
from graph import Graph

def bfs(graph, type=SearchType.graph):
    if type is SearchType.graph:
        print("GraphIII")
    else:
        print("TreeIII")


if __name__ == '__main__':
    g = Graph()
    bfs(g, SearchType.tree)
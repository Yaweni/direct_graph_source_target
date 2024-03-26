import networkx as nx
from collections import deque
import networkx as nx


def transform_to_directed(graph, source, destination):
    directed_graph = nx.DiGraph()
    directed_graph.add_nodes_from(graph.nodes())

    queue = deque([(destination, None)])
    visited = set()

    while queue:
        current, parent = queue.popleft()
        visited.add(current)

        if current == source:
            neighbors = graph.neighbors(current)
            for neighbor in neighbors:
                directed_graph.add_edge(current, neighbor)

        else:
            neighbors = graph.neighbors(current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    directed_graph.add_edge(neighbor, current)
                    queue.append((neighbor, None))

    return directed_graph

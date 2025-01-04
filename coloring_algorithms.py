from imports import *

def largest_first(graph: nx.Graph) -> Dict[int, int]:

    nodes_sorted = sorted(
        graph.nodes, key=lambda node: graph.degree[node], reverse=True
    )

    coloring: Dict[int, int] = {}

    for node in nodes_sorted:

        neighbor_colors = {
            coloring[neighbor]
            for neighbor in graph.neighbors(node)
            if neighbor in coloring
        }

        color = 0
        while color in neighbor_colors:
            color += 1

        coloring[node] = color

    return coloring

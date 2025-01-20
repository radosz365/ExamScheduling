from imports import *


def largest_first(graph: nx.Graph) -> Dict[int, int]:
    """
    Perform graph coloring using the Largest First heuristic.

    Args:
        graph (nx.Graph): The input graph to be colored.

    Returns:
        Dict[int, int]: A dictionary mapping nodes to their assigned colors.

    The Largest First heuristic sorts the nodes by degree in descending order
    and assigns the smallest available color to each node, ensuring no two adjacent
    nodes share the same color.
    """
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

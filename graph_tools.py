from imports import *


def add_edges(df: pd.DataFrame, graph: nx.Graph, group_column: str) -> nx.Graph:
    """
    Add edges to a graph based on group membership.

    Args:
        df (pd.DataFrame): DataFrame containing data to group nodes by.
        graph (nx.Graph): The graph to which edges will be added.
        group_column (str): The column name in the DataFrame used to define groups.

    Returns:
        nx.Graph: The updated graph with edges added between nodes in the same group.

    This function groups the DataFrame by the specified column and connects
    all nodes within each group in the graph.
    """
    grouped = df.groupby(group_column)

    for group, indices in grouped.groups.items():
        indices_list = list(indices)
        for i in range(len(indices_list)):
            for j in range(i + 1, len(indices_list)):
                graph.add_edge(indices_list[i], indices_list[j])

    return graph


def visualize_graph(graph: nx.Graph) -> None:
    """
    Visualize the structure of a graph using Matplotlib.

    Args:
        graph (nx.Graph): The graph to be visualized.

    This function displays the graph with labeled nodes and styled edges.
    """
    plt.figure(figsize=(8, 6))

    nx.draw(
        graph,
        with_labels=True,
        node_color="lightblue",
        node_size=500,
        font_size=10,
        font_color="black",
        edge_color="gray",
    )

    plt.title("Graph Visualization")
    plt.show()

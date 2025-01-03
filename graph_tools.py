from imports import *


def add_edges(df, graph, group_column):

    grouped = df.groupby(group_column)

    for group, indices in grouped.groups.items():
        indices_list = list(indices)
        for i in range(len(indices_list)):
            for j in range(i + 1, len(indices_list)):
                graph.add_edge(indices_list[i], indices_list[j])

    return graph


def visualize_graph(graph):

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

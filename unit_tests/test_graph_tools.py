import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from graph_tools import add_edges
from imports import *


# --- Tests for add_edges ---
def test_empty_dataframe() -> None:
    """
    Test adding edges to a graph with an empty DataFrame.

    Asserts:
        Ensures that the graph remains empty when no data is provided.
    """
    df: pd.DataFrame = pd.DataFrame(columns=["group", "value"])
    graph: nx.Graph = nx.Graph()
    result_graph: nx.Graph = add_edges(df, graph, "group")

    assert len(result_graph.nodes) == 0, "The graph should remain empty."
    assert len(result_graph.edges) == 0, "The graph should have no edges."


def test_multiple_groups() -> None:
    """
    Test adding edges to a graph with multiple groups in the DataFrame.

    Asserts:
        Ensures that edges are correctly added between nodes in the same group.
    """
    data: dict[str, list[Any]] = {"group": ["A", "A", "B", "B", "C"], "value": [1, 2, 3, 4, 5]}
    df: pd.DataFrame = pd.DataFrame(data)
    graph: nx.Graph = nx.Graph()
    result_graph: nx.Graph = add_edges(df, graph, "group")

    assert result_graph.has_edge(0, 1), "Missing edge in group A."
    assert result_graph.has_edge(2, 3), "Missing edge in group B."
    assert not result_graph.has_edge(4, 4), "Unexpected edge in group C."


if __name__ == "__main__":
    pytest.main([__file__])

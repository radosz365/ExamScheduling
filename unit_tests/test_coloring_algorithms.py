import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from coloring_algorithms import largest_first
from imports import *


# --- Tests for largest_first ---
def test_largest_first_vs_networkx() -> None:
    """
    Test the largest_first coloring algorithm against NetworkX's implementation.

    Asserts:
        Ensures the custom implementation produces a comparable number of colors
        to NetworkX's greedy coloring using the 'largest_first' strategy.
    """
    G: nx.Graph = nx.erdos_renyi_graph(10, 0.5, seed=42)

    custom_coloring: Dict[int, int] = largest_first(G)

    nx_coloring: Dict[int, int] = nx.coloring.greedy_color(G, strategy="largest_first")

    custom_color_count: int = len(set(custom_coloring.values()))
    nx_color_count: int = len(set(nx_coloring.values()))

    assert abs(custom_color_count - nx_color_count) <= nx_color_count * 0.1


if __name__ == "__main__":
    pytest.main([__file__])

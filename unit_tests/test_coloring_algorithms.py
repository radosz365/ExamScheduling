import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from coloring_algorithms import largest_first
from imports import *


# --- Tests for largest_first ---
def test_largest_first_vs_networkx():

    G = nx.erdos_renyi_graph(10, 0.5, seed=42)

    custom_coloring = largest_first(G)

    nx_coloring = nx.coloring.greedy_color(G, strategy="largest_first")

    custom_color_count = len(set(custom_coloring.values()))
    nx_color_count = len(set(nx_coloring.values()))

    assert abs(custom_color_count - nx_color_count) <= nx_color_count * 0.1


if __name__ == "__main__":
    pytest.main([__file__])

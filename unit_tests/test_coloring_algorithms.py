import pytest
import networkx as nx
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from coloring_algorithms import largest_first

# --- Tests for largest_first ---
def test_largest_first_vs_networkx():
    
    G = nx.erdos_renyi_graph(10, 0.5, seed=42)

    custom_coloring = largest_first(G)

    nx_coloring = nx.coloring.greedy_color(G, strategy="largest_first")

    custom_colors = {frozenset([node for node, color in custom_coloring.items() if color == c]) for c in set(custom_coloring.values())}
    nx_colors = {frozenset([node for node, color in nx_coloring.items() if color == c]) for c in set(nx_coloring.values())}

    assert custom_colors == nx_colors

if __name__ == "__main__":
    pytest.main([__file__])
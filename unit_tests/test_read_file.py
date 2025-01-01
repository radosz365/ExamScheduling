import unittest
import networkx as nx
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from read_file import create_grapf_from_csv

class TestGraphCreation(unittest.TestCase):
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            create_grapf_from_csv("niema.csv")

    def test_empty_file(self):
        temp_file = "datasets/empty.csv"
        with open(temp_file, "w") as f:
            pass
        try:
            with self.assertRaises(ValueError):
                create_grapf_from_csv("empty.csv")
        finally:
            os.remove(temp_file)

    def test_invalid_csv_format(self):
        temp_file = "datasets/invalid.csv"
        with open(temp_file, "w") as f:
            f.write("invalid,data\n1,2,3")
        try:
            with self.assertRaises(ValueError):
                create_grapf_from_csv("invalid.csv")
        finally:
            os.remove(temp_file)

    def test_graph_creation(self):
        temp_file = "datasets/valid.csv"
        with open(temp_file, "w") as f:
            f.write("course,lecturer,group,classroom\nMath,John,A,101\nPhysics,Emma,B,102")
        try:
            graph, _ = create_grapf_from_csv("valid.csv")
            self.assertIsInstance(graph, nx.Graph)
            self.assertGreater(len(graph.nodes), 0)
        finally:
            os.remove(temp_file)

if __name__ == "__main__":
    unittest.main()

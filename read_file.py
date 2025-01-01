import pandas as pd
import networkx as nx
import os
import csv

class Node:
    def __init__(self, course, lecturer, group, classrom):
        self.course = course
        self.lecturer = lecturer
        self.group = group
        self.classrom = classrom

    def __str__(self):
        return f"{self.course} {self.lecturer} {self.group} {self.classrom}"

def create_grapf_from_csv(filename):
    G = nx.Graph()
    file_path = os.path.join("datasets", filename)

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file does not exist.")

        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError(f"The file is empty.")

        required_columns = {"course", "lecturer", "group", "classroom"}

        if not required_columns.issubset(df.columns):
            raise ValueError(f"Invalid CSV format. Missing required columns.")

        for index, row in df.iterrows():
            node = Node(row["course"], row["lecturer"], row["group"], row["classroom"])
            G.add_node(index, data=node)

    except pd.errors.ParserError as e:
        raise csv.Error(f"Error while parsing the CSV file: {e}")

    return G, df

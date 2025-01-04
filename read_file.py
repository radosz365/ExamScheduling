from imports import *


class Node:
    """
    Represents a node in the graph with course, lecturer, group, and classroom details.
    """

    def __init__(self, course: str, lecturer: str, group: str, classroom: str) -> None:
        """
        Initialize a Node object.

        Args:
            course (str): Name of the course.
            lecturer (str): Name of the lecturer.
            group (str): Group identifier.
            classroom (str): Classroom identifier.
        """
        self.course: str = course
        self.lecturer: str = lecturer
        self.group: str = group
        self.classroom: str = classroom

    def __str__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            str: String containing course, lecturer, group, and classroom details.
        """
        return f"{self.course} {self.lecturer} {self.group} {self.classroom}"


def create_graph_from_csv(filename: str) -> Tuple[nx.Graph, pd.DataFrame]:
    """
    Create a graph and a DataFrame from a CSV file.

    Args:
        filename (str): The name of the CSV file located in the 'datasets' directory.

    Returns:
        Tuple[nx.Graph, pd.DataFrame]: A tuple containing the graph and the corresponding DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or missing required columns.
        csv.Error: If there is a parsing error in the CSV file.
    """
    G: nx.Graph = nx.Graph()
    file_path: str = os.path.join("datasets", filename)

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("The file does not exist.")

        df: pd.DataFrame = pd.read_csv(file_path)

        if df.empty:
            raise ValueError("The file is empty.")

        required_columns = {"course", "lecturer", "group", "classroom"}

        if not required_columns.issubset(df.columns):
            raise ValueError("Invalid CSV format. Missing required columns.")

        for index, row in df.iterrows():
            node = Node(row["course"], row["lecturer"], row["group"], row["classroom"])
            G.add_node(index, data=node)

    except pd.errors.ParserError as e:
        raise csv.Error(f"Error while parsing the CSV file: {e}")

    return G, df

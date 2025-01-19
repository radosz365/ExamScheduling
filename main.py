from imports import *
from schedule_tools import save_schedule_to_csv, calculate_schedule_range
from assign_slots import assign_time_slots
from graph_tools import add_edges
from read_file import create_graph_from_csv


def create_schedule(dataset: str, start_date: str, time_slots: List[str]) -> str:
    """
    Create an exam schedule based on the provided dataset, start date, and time slots.

    Args:
        dataset (str): The name of the dataset file to load.
        start_date (str): The starting date for the schedule.
        time_slots (List[str]): A list of available time slots for scheduling.

    Returns:
        str: A message indicating the computation time for the schedule creation.
    """
    start_time: float = time.time()

    G1: nx.Graph
    df: pd.DataFrame
    G1, df = create_graph_from_csv(dataset)

    G1 = add_edges(df, G1, "group")
    df["primary_color"] = df.index.map(
        nx.coloring.greedy_color(G1, strategy="largest_first")
    )
    G1.clear_edges()

    G1 = add_edges(df, G1, "classroom")
    G1 = add_edges(df, G1, "lecturer")
    df["secondary_color"] = df.index.map(
        nx.coloring.greedy_color(G1, strategy="largest_first")
    )

    assign_time_slots(df, start_date, time_slots)
    output_path: str = f"schedules/schedule_{dataset}"
    save_schedule_to_csv(df, output_path)
    calculate_schedule_range(df)

    end_time: float = time.time()
    elapsed_time: float = end_time - start_time

    return f"Computation time: {elapsed_time:.2f} s"

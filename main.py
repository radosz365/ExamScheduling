from imports import *
from schedule_tools import save_schedule_to_csv, calculate_schedule_range
from assign_slots import assign_time_slots
from graph_tools import add_edges, visualize_graph
from read_file import create_graph_from_csv


def create_schedule(dataset, start_date, time_slots):
    start_time = time.time()

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
    save_schedule_to_csv(df, dataset)
    calculate_schedule_range(df)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return f"Computation time: {elapsed_time:.2f} s"

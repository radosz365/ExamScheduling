from imports import *
from schedule_tools import save_schedule_to_csv, calculate_schedule_range
from assign_slots import assign_time_slots
from graph_tools import add_edges, visualize_graph
from read_file import create_graph_from_csv

"""
Main script for generating an exam schedule.

This script reads a dataset, creates a graph structure, applies graph coloring, 
assigns time slots to exams, and saves the resulting schedule to a file. 
It also measures the computation time.
"""

dataset: str = "dataset1000.csv"
"""
Path to the input dataset CSV file.
"""

start_date: str = "30.01.2025"
"""
Start date for the schedule.
"""

time_slots: List[str] = [
    "8:00-8:45",
    "9:00-9:45",
    "10:00-10:45",
    "11:00-11:45",
    "12:00-12:45",
    "13:00-13:45",
    "14:00-14:45",
    "15:00-15:45",
    "16:00-16:45",
]
"""
List of available time slots for scheduling.
"""

start_time: float = time.time()
"""
Start time of the computation process.
"""

G1: nx.Graph
df: pd.DataFrame
G1, df = create_graph_from_csv(dataset)
"""
Load the dataset and create a graph representation.
"""

G1 = add_edges(df, G1, "group")
df["primary_color"] = df.index.map(
    nx.coloring.greedy_color(G1, strategy="largest_first")
)
G1.clear_edges()
"""
Add edges to the graph based on group constraints and apply primary graph coloring.
"""

G1 = add_edges(df, G1, "classroom")
G1 = add_edges(df, G1, "lecturer")
df["secondary_color"] = df.index.map(
    nx.coloring.greedy_color(G1, strategy="largest_first")
)
"""
Add edges to the graph based on classroom and lecturer constraints 
and apply secondary graph coloring.
"""

assign_time_slots(df, start_date, time_slots)
"""
Assign time slots to the dataset based on the graph coloring and constraints.
"""

save_schedule_to_csv(df, "schedules/schedule1000.csv")
"""
Save the final schedule to a CSV file.
"""

calculate_schedule_range(df)
"""
Calculate and display the total range of the schedule in days.
"""

end_time: float = time.time()
elapsed_time: float = end_time - start_time
"""
End time of the computation process and calculate elapsed time.
"""

print(f"Computation time: {elapsed_time:.2f} s")
"""
Print the total computation time in seconds.
"""

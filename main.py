from imports import *
from schedule_tools import save_schedule_to_csv, calculate_schedule_range
from assign_slots import assign_time_slots
from graph_tools import add_edges, visualize_graph
from read_file import create_graph_from_csv

dataset = "dataset1000.csv"

start_date = "30.01.2025"

time_slots = [
    "8:00-8:45",
    "9:00-9:45",
    "10:00-10:45", 
    "11:00-11:45",
    "12:00-12:45", 
    "13:00-13:45", 
    "14:00-14:45", 
    "15:00-15:45",
    "16:00-16:45"
]

start_time = time.time()

G1, df = create_graph_from_csv(dataset)

G1 = add_edges(df, G1, "group")
df["primary_color"] = df.index.map(nx.coloring.greedy_color(G1, strategy="largest_first"))
G1.clear_edges()

G1 = add_edges(df, G1, "classroom")
G1 = add_edges(df, G1, "lecturer")
df["secondary_color"] = df.index.map(nx.coloring.greedy_color(G1, strategy="largest_first"))

assign_time_slots(df, start_date, time_slots)
save_schedule_to_csv(df, "schedules/schedule1000.csv")
calculate_schedule_range(df)

end_time = time.time() 
elapsed_time = end_time - start_time
print(f"Computation time: {elapsed_time:.2f} s")
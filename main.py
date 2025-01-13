from imports import *
from schedule_tools import save_schedule_to_csv, calculate_schedule_range
from assign_slots import assign_time_slots
from graph_tools import add_edges
from read_file import create_graph_from_csv
from visualization_for_students import create_exam_schedule_png



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
    output_path = f"schedules/schedule_{dataset}"
    save_schedule_to_csv(df, output_path)
    calculate_schedule_range(df)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return f"Computation time: {elapsed_time:.2f} s"

# function to create exam schedule png for students for a specific file
def create_exam_schedule_png_for_students(group_to_display):
    file_path = "schedules/schedule1000.csv"
    create_exam_schedule_png(file_path, group_to_display)

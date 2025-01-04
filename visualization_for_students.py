from imports import *

file_path: str = "schedules/schedule1000.csv"
"""
Path to the input CSV file containing the schedule data.
"""

data: DataFrame = pd.read_csv(file_path)
"""
DataFrame holding the raw schedule data loaded from the CSV file.
"""

all_time_slots: List[str] = data["time"].dropna().unique().tolist()
"""
List of all unique time slots available in the schedule.
"""

group_to_display: str = "UDT.FC6.DKR.6724.SZY"
"""
The specific group to visualize in the exam schedule.
"""

data = data[data["group"] == group_to_display]
"""
Filter the schedule data for the selected group.
"""

data["datetime"] = data["date"] + " " + data["time"]
"""
Combine the 'date' and 'time' columns into a single datetime string.
"""

data["date"] = pd.to_datetime(data["date"], dayfirst=True)
"""
Convert the 'date' column to a datetime object.
"""

data["time_slot"] = data["time"]
"""
Alias the 'time' column as 'time_slot' for clarity.
"""

unique_dates = data["date"].unique()
"""
Array of unique dates in the filtered schedule data.
"""

full_index = pd.MultiIndex.from_product(
    [all_time_slots, unique_dates], names=["time_slot", "date"]
)
"""
MultiIndex object combining all time slots and dates.
"""

data = data.set_index(["time_slot", "date"]).reindex(full_index).reset_index()
"""
Align the data to the full index of time slots and dates, filling missing values.
"""

data["details"] = data["course"] + ", " + data["lecturer"] + ", " + data["classroom"]
"""
Concatenate course, lecturer, and classroom details into a single string.
"""

pivot_table: DataFrame = data.pivot_table(
    index="time_slot",
    columns="date",
    values="details",
    aggfunc=lambda x: "\n".join(x) if pd.notna(x).any() else "",
)
"""
Pivot table summarizing the schedule by time slot and date.
"""

pivot_table = pivot_table.replace("", pd.NA).dropna(how="all")
"""
Replace empty strings with NaN and drop rows/columns with all NaN values.
"""

pivot_table = pivot_table.reindex(all_time_slots).dropna(how="all")
"""
Ensure the pivot table is aligned to the original time slots and drop NaN rows.
"""

def wrap_text(text: str, width: int = 15) -> str:
    """
    Wrap text to fit within a specified width.

    Args:
        text (str): The input text to wrap.
        width (int): The maximum width of each line.

    Returns:
        str: Wrapped text with line breaks.
    """
    if pd.isna(text) or not text.strip():
        return ""
    return "\n".join(textwrap.wrap(text, width=width))


fig, ax = plt.subplots(figsize=(14, 10))
ax.set_axis_off()
"""
Initialize a Matplotlib figure and axis for table visualization.
"""

table = Table(ax, bbox=[0, 0, 1, 1])
"""
Create a Matplotlib Table object for visualizing the schedule.
"""

n_cols: int = len(pivot_table.columns)
"""
Number of columns in the pivot table.
"""

n_rows: int = len(pivot_table.index) + 1
"""
Number of rows in the pivot table (including the header row).
"""

header_cell = table.add_cell(
    0, 0, width=2, height=0.5, text="Time / Date", loc="center", facecolor="lightgrey"
)
header_cell.get_text().set_fontsize(14)
header_cell.get_text().set_weight("bold")
"""
Add the header cell for the time/date column in the table.
"""

for col, date in enumerate(pivot_table.columns):
    cell = table.add_cell(
        0,
        col + 1,
        width=1.5,
        height=0.5,
        text=date.strftime("%Y-%m-%d"),
        loc="center",
        facecolor="lightgrey",
    )
    cell.get_text().set_fontsize(14)
    cell.get_text().set_weight("bold")
"""
Add header cells for each date in the table.
"""

for row, time_slot in enumerate(pivot_table.index):
    cell = table.add_cell(
        row + 1,
        0,
        width=2,
        height=0.5,
        text=time_slot,
        loc="center",
        facecolor="lightgrey",
    )
    cell.get_text().set_fontsize(12)
    for col, date in enumerate(pivot_table.columns):
        value = pivot_table.loc[time_slot, date]
        wrapped_value = wrap_text(value, width=15)
        cell = table.add_cell(
            row + 1,
            col + 1,
            width=1.5,
            height=0.5,
            text=wrapped_value,
            loc="center",
            facecolor="white",
        )
        cell.get_text().set_fontsize(12)
"""
Add data cells to the table for each time slot and date.
"""

ax.add_table(table)
"""
Add the table to the axis.
"""

plt.title(f"Exam schedule for group: {group_to_display}", fontsize=18, pad=20)
plt.show()
"""
Display the table with the schedule visualization.
"""

folder_path: str = "visualizations"
os.makedirs(folder_path, exist_ok=True)
"""
Create the directory for saving visualizations if it doesn't exist.
"""

output_file_path: str = f"visualizations/{group_to_display.replace('.', '_')}.png"
fig.savefig(output_file_path, dpi=300, bbox_inches="tight")
"""
Save the visualization as a PNG file in the specified directory.
"""
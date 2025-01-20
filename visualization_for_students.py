from imports import *


def wrap_text(text: str, width: int = 15) -> str:
    """
    Wrap text to fit within a specified width.

    Args:
        text (str): The input text to be wrapped.
        width (int): The maximum width of each line.

    Returns:
        str: Wrapped text with line breaks.
    """
    if pd.isna(text) or not text.strip():
        return ""
    return "\n".join(textwrap.wrap(text, width=width))


def create_exam_schedule_png(file_path: str, group_to_display: str) -> None:
    """
    Create and save a visual representation of the exam schedule for a specific group.

    Args:
        file_path (str): Path to the input CSV file containing the schedule data.
        group_to_display (str): The group for which the schedule will be visualized.

    Returns:
        None
    """
    data: pd.DataFrame = pd.read_csv(file_path)

    all_time_slots: List[str] = data["time"].dropna().unique().tolist()
    data = data[data["group"] == group_to_display]

    data["datetime"] = data["date"] + " " + data["time"]
    data["date"] = pd.to_datetime(data["date"], dayfirst=True)
    data["time_slot"] = data["time"]

    unique_dates: List[pd.Timestamp] = data["date"].unique()
    full_index = pd.MultiIndex.from_product(
        [all_time_slots, unique_dates], names=["time_slot", "date"]
    )
    data = data.set_index(["time_slot", "date"]).reindex(full_index).reset_index()
    data["details"] = (
        data["course"] + ", " + data["lecturer"] + ", " + data["classroom"]
    )

    pivot_table: pd.DataFrame = data.pivot_table(
        index="time_slot",
        columns="date",
        values="details",
        aggfunc=lambda x: "\n".join(x) if pd.notna(x).any() else "",
    )

    pivot_table = pivot_table.replace("", pd.NA).dropna(how="all")
    pivot_table = pivot_table.reindex(all_time_slots).dropna(how="all")

    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_axis_off()

    table = Table(ax, bbox=[0, 0, 1, 1])

    header_cell = table.add_cell(
        0,
        0,
        width=2,
        height=0.5,
        text="Time / Date",
        loc="center",
        facecolor="lightgrey",
    )
    header_cell.get_text().set_fontsize(14)
    header_cell.get_text().set_weight("bold")

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

    ax.add_table(table)

    plt.title(f"Exam schedule for group: {group_to_display}", fontsize=18, pad=20)

    folder_path: str = "visualizations"
    os.makedirs(folder_path, exist_ok=True)
    output_file_path: str = f"{folder_path}/{group_to_display.replace('.', '_')}.png"
    fig.savefig(output_file_path, dpi=300, bbox_inches="tight")

    print(f"Schedule visualization saved to {output_file_path}")


def create_exam_schedule_png_for_all_groups(file_path: str) -> None:
    """
    Create and save visual representations of the exam schedules for all groups.

    Args:
        file_path (str): Path to the input CSV file containing the schedule data.

    Returns:
        None
    """
    data: pd.DataFrame = pd.read_csv(file_path)
    groups: List[str] = data["group"].unique().tolist()
    for group in groups:
        create_exam_schedule_png(file_path, group)
    print("All schedules have been saved to visualizations folder")

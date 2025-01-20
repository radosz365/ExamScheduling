from imports import *


def assign_time_slots(df: pd.DataFrame, start_date: str, time_slots: List[str]) -> pd.DataFrame:
    """
    Assign time slots and dates to exams based on graph coloring.

    Args:
        df (pd.DataFrame): DataFrame containing exam data with required columns:
            'course', 'lecturer', 'group', 'classroom', 'primary_color', and 'secondary_color'.
        start_date (str): The starting date for scheduling in the format 'dd.mm.yyyy'.
        time_slots (List[str]): A list of available time slots.

    Returns:
        pd.DataFrame: Updated DataFrame with 'date' and 'time' columns assigned.

    Raises:
        ValueError: If required columns are missing, start_date is incorrectly formatted,
                    or time_slots is not a non-empty list.
    """
    if not {
        "course",
        "lecturer",
        "group",
        "classroom",
        "primary_color",
        "secondary_color",
    }.issubset(df.columns):
        raise ValueError("Missing required columns.")

    try:
        current_date: datetime = datetime.strptime(start_date, "%d.%m.%Y")
    except ValueError:
        raise ValueError("The start_date is not in the correct format.")

    if not time_slots or not isinstance(time_slots, list):
        raise ValueError("The 'time_slots' variable must be a non-empty list.")

    unique_primary_colors: List[int] = df["primary_color"].unique().tolist()

    df["date"] = None
    df["time"] = None

    slot_iterator = iter(time_slots)
    current_slot: str = next(slot_iterator)

    for unique_primary_color in unique_primary_colors:
        unique_secondary_colors: List[int] = (
            df[df["primary_color"] == unique_primary_color]["secondary_color"]
            .unique()
            .tolist()
        )

        for unique_secondary_color in unique_secondary_colors:
            while current_date.weekday() in [5, 6]:
                current_date += timedelta(days=1)

            df.loc[
                (df["primary_color"] == unique_primary_color)
                & (df["secondary_color"] == unique_secondary_color),
                ["date", "time"],
            ] = [current_date.strftime("%d.%m.%Y"), current_slot]

            try:
                current_slot = next(slot_iterator)
            except StopIteration:
                slot_iterator = iter(time_slots)
                current_slot = next(slot_iterator)
                current_date += timedelta(days=1)

        if current_slot != time_slots[0]:
            slot_iterator = iter(time_slots)
            current_slot = next(slot_iterator)
            current_date += timedelta(days=1)
        
        # even if there are still free slots on a given day,
        # we skip to the next day to avoid a situation where
        # one group have 2 exams in one day

    return df

import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from imports import *

schedule_file = "schedules/schedule_dataset1000.csv"


def load_schedule() -> DataFrame:
    """
    Load the schedule CSV into a Pandas DataFrame.

    Returns:
        DataFrame: The schedule data with an additional 'datetime' column.
    """
    data: DataFrame = pd.read_csv(schedule_file)
    data["datetime"] = data["date"] + " " + data["time"]
    return data


def test_no_lecturer_conflicts() -> None:
    """
    Ensure no lecturer has two exams in the same time slot.

    Asserts:
        No conflicts exist where a lecturer is assigned more than one exam in the same slot.
    """
    data: DataFrame = load_schedule()
    conflicts: Any = data.groupby(["datetime", "lecturer"]).size()
    assert all(
        conflicts <= 1
    ), "A lecturer has more than one exam in the same time slot."


def test_no_classroom_conflicts() -> None:
    """
    Ensure no classroom has two exams in the same time slot.

    Asserts:
        No conflicts exist where a classroom is assigned more than one exam in the same slot.
    """
    data: DataFrame = load_schedule()
    conflicts: Any = data.groupby(["datetime", "classroom"]).size()
    assert all(
        conflicts <= 1
    ), "A classroom has more than one exam in the same time slot."


def test_no_group_conflicts_same_slot() -> None:
    """
    Ensure no group has two exams in the same time slot.

    Asserts:
        No conflicts exist where a group is assigned more than one exam in the same slot.
    """
    data: DataFrame = load_schedule()
    conflicts: Any = data.groupby(["datetime", "group"]).size()
    assert all(conflicts <= 1), "A group has more than one exam in the same time slot."


def test_no_group_multiple_exams_per_day() -> None:
    """
    Ensure no group has more than one exam on the same day.

    Asserts:
        No conflicts exist where a group is assigned multiple exams on the same day.
    """
    data: DataFrame = load_schedule()
    data["date"] = data["datetime"].str.split(" ").str[0]
    conflicts: Any = data.groupby(["date", "group"]).size()
    assert all(conflicts <= 1), "A group has more than one exam on the same day."


def test_no_exams_on_weekends() -> None:
    """
    Ensure no exams are scheduled on weekends.

    Asserts:
        No exams are assigned to weekends based on the weekday calculation.
    """
    data: DataFrame = load_schedule()
    data["date"] = pd.to_datetime(
        data["datetime"].str.split(" ").str[0], format="%d.%m.%Y"
    )
    weekends: pd.Series = data["date"].dt.weekday >= 5
    assert not any(weekends), "An exam is scheduled on a weekend."


if __name__ == "__main__":
    pytest.main([__file__])

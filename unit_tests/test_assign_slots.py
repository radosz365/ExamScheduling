import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from assign_slots import assign_time_slots
from imports import *


def create_valid_dataframe() -> pd.DataFrame:
    """
    Create a valid DataFrame for testing.

    Returns:
        pd.DataFrame: A DataFrame with sample data for scheduling.
    """
    return pd.DataFrame(
        {
            "course": ["Math", "Science", "Chemistry"],
            "lecturer": ["James", "Emma", "Henry"],
            "group": ["A", "B", "C"],
            "classroom": [101, 102, 103],
            "primary_color": [1, 2, 3],
            "secondary_color": [1, 2, 3],
        }
    )


def validate_result(result: pd.DataFrame, ensure_no_weekends: bool = False) -> None:
    """
    Validate the resulting DataFrame for correct structure and constraints.

    Args:
        result (pd.DataFrame): The DataFrame to validate.
        ensure_no_weekends (bool): Flag to check if weekends are excluded.
    """
    assert "date" in result.columns
    assert "time" in result.columns
    assert all(result["date"].notnull())
    assert all(result["time"].notnull())
    if ensure_no_weekends:
        weekend_days: List[int] = [
            datetime.strptime(date, "%d.%m.%Y").weekday() for date in result["date"]
        ]
        assert all(day not in [5, 6] for day in weekend_days)


def test_valid_input() -> None:
    """
    Test assigning time slots with valid input data.
    """
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "01.01.2024"
    time_slots: List[str] = ["10:00", "11:00", "12:00"]

    result: pd.DataFrame = assign_time_slots(df, start_date, time_slots)
    validate_result(result)


def test_missing_required_columns() -> None:
    """
    Test assigning time slots when required columns are missing.

    Asserts:
        Raises ValueError if the DataFrame is missing required columns.
    """
    df: pd.DataFrame = pd.DataFrame(
        {
            "course": ["Math", "Science"],
            "lecturer": ["James", "Emma"],
            "group": ["A", "B"],
        }
    )
    start_date: str = "01.01.2024"
    time_slots: List[str] = ["10:00", "11:00"]

    with pytest.raises(ValueError):
        assign_time_slots(df, start_date, time_slots)


def test_invalid_date_format() -> None:
    """
    Test assigning time slots with an invalid date format.

    Asserts:
        Raises ValueError for incorrect date formats.
    """
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "01-01-2024"
    time_slots: List[str] = ["10:00", "11:00"]

    with pytest.raises(ValueError):
        assign_time_slots(df, start_date, time_slots)


def test_empty_time_slots() -> None:
    """
    Test assigning time slots when no time slots are provided.

    Asserts:
        Raises ValueError for an empty time slot list.
    """
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "01.01.2024"
    time_slots: List[str] = []

    with pytest.raises(ValueError):
        assign_time_slots(df, start_date, time_slots)


def test_invalid_time_slots() -> None:
    """
    Test assigning time slots with invalid time slot data.

    Asserts:
        Raises ValueError if time slots are not a valid list.
    """
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "01.01.2024"
    time_slots: Any = "11:00"

    with pytest.raises(ValueError):
        assign_time_slots(df, start_date, time_slots)


def test_handles_weekends() -> None:
    """
    Test assigning time slots while avoiding weekends.

    Asserts:
        Validates that no exams are scheduled on weekends.
    """
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "05.01.2024"
    time_slots: List[str] = ["10:00", "11:00", "12:00"]

    result: pd.DataFrame = assign_time_slots(df, start_date, time_slots)
    validate_result(result, ensure_no_weekends=True)


if __name__ == "__main__":
    pytest.main([__file__])

import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from assign_slots import assign_time_slots
from imports import *


def create_valid_dataframe() -> pd.DataFrame:
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
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "01.01.2024"
    time_slots: List[str] = ["10:00", "11:00", "12:00"]

    result: pd.DataFrame = assign_time_slots(df, start_date, time_slots)
    validate_result(result)


def test_missing_required_columns() -> None:
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
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "01-01-2024"
    time_slots: List[str] = ["10:00", "11:00"]

    with pytest.raises(ValueError):
        assign_time_slots(df, start_date, time_slots)


def test_empty_time_slots() -> None:
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "01.01.2024"
    time_slots: List[str] = []

    with pytest.raises(ValueError):
        assign_time_slots(df, start_date, time_slots)


def test_invalid_time_slots() -> None:
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "01.01.2024"
    time_slots: Any = "11:00"

    with pytest.raises(ValueError):
        assign_time_slots(df, start_date, time_slots)


def test_handles_weekends() -> None:
    df: pd.DataFrame = create_valid_dataframe()
    start_date: str = "05.01.2024"
    time_slots: List[str] = ["10:00", "11:00", "12:00"]

    result: pd.DataFrame = assign_time_slots(df, start_date, time_slots)
    validate_result(result, ensure_no_weekends=True)


if __name__ == "__main__":
    pytest.main([__file__])

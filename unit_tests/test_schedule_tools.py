import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schedule_tools import save_schedule_to_csv, calculate_schedule_range
from imports import *


# --- Tests for save_schedule_to_csv ---
def create_test_dataframe() -> DataFrame:
    return pd.DataFrame(
        {
            "course": ["Math", "Physics", "Chemistry"],
            "lecturer": ["James", "Emma", "Henry"],
            "group": ["A", "B", "C"],
            "classroom": ["101", "102", "103"],
            "date": ["2024-12-01", "2024-12-02", "2024-12-03"],
            "time": ["10:00", "11:00", "12:00"],
            "primary_color": [1, 2, 3],
            "secondary_color": [1, 2, 3],
        }
    )


def test_file_saving() -> None:
    df: DataFrame = create_test_dataframe()
    output_path: str = "test_schedule.csv"

    save_schedule_to_csv(df, output_path)
    assert os.path.exists(output_path), "The file was not saved."
    os.remove(output_path)


def test_columns_removed() -> None:
    df: DataFrame = create_test_dataframe()
    output_path: str = "test_schedule.csv"

    save_schedule_to_csv(df, output_path)
    saved_df: DataFrame = pd.read_csv(output_path)
    assert (
        "primary_color" not in saved_df.columns
    ), "The 'primary_color' column was not removed."
    assert (
        "secondary_color" not in saved_df.columns
    ), "The 'secondary_color' column was not removed."
    os.remove(output_path)


def test_missing_columns() -> None:
    df: DataFrame = pd.DataFrame({"course": ["Math", "Physics", "Chemistry"]})
    output_path: str = "test_schedule.csv"

    with pytest.raises(ValueError):
        save_schedule_to_csv(df, output_path)


# --- Tests for calculate_schedule_range ---
def test_calculate_schedule_range_valid_dates() -> None:
    data: dict[str, list[str]] = {"date": ["01.01.2024", "05.01.2024", "10.01.2024"]}
    df: DataFrame = pd.DataFrame(data)

    expected_range: int = 10

    assert calculate_schedule_range(df) == expected_range


def test_calculate_schedule_range_single_date() -> None:
    data: dict[str, list[str]] = {"date": ["01.01.2024"]}
    df: DataFrame = pd.DataFrame(data)

    expected_range: int = 1

    assert calculate_schedule_range(df) == expected_range


def test_calculate_schedule_range_empty_dataframe() -> None:
    df: DataFrame = pd.DataFrame({"date": []})

    with pytest.raises(ValueError):
        calculate_schedule_range(df)


def test_calculate_schedule_range_invalid_dates() -> None:
    data: dict[str, list[str]] = {"date": ["2024-01-01", "2024-01-05"]}
    df: DataFrame = pd.DataFrame(data)

    with pytest.raises(ValueError):
        calculate_schedule_range(df)


if __name__ == "__main__":
    pytest.main([__file__])

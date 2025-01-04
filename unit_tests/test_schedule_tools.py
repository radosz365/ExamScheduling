import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schedule_tools import save_schedule_to_csv, calculate_schedule_range
from imports import *


# --- Tests for save_schedule_to_csv ---
def create_test_dataframe() -> DataFrame:
    """
    Create a sample DataFrame for testing.

    Returns:
        DataFrame: A DataFrame with sample data for scheduling.
    """
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
    """
    Test saving the schedule to a CSV file.

    Asserts:
        Ensures the file is saved to the specified path.
    """
    df: DataFrame = create_test_dataframe()
    output_path: str = "test_schedule.csv"

    save_schedule_to_csv(df, output_path)
    assert os.path.exists(output_path), "The file was not saved."
    os.remove(output_path)


def test_columns_removed() -> None:
    """
    Test if unnecessary columns are removed when saving the schedule.

    Asserts:
        Ensures that 'primary_color' and 'secondary_color' are not present in the saved file.
    """
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
    """
    Test saving the schedule with missing required columns.

    Asserts:
        Raises ValueError if required columns are missing in the DataFrame.
    """
    df: DataFrame = pd.DataFrame({"course": ["Math", "Physics", "Chemistry"]})
    output_path: str = "test_schedule.csv"

    with pytest.raises(ValueError):
        save_schedule_to_csv(df, output_path)


# --- Tests for calculate_schedule_range ---
def test_calculate_schedule_range_valid_dates() -> None:
    """
    Test calculating the schedule range with valid dates.

    Asserts:
        The calculated range matches the expected range.
    """
    data: dict[str, list[str]] = {"date": ["01.01.2024", "05.01.2024", "10.01.2024"]}
    df: DataFrame = pd.DataFrame(data)

    expected_range: int = 10

    assert calculate_schedule_range(df) == expected_range


def test_calculate_schedule_range_single_date() -> None:
    """
    Test calculating the schedule range with a single date.

    Asserts:
        The calculated range is 1 for a single date.
    """
    data: dict[str, list[str]] = {"date": ["01.01.2024"]}
    df: DataFrame = pd.DataFrame(data)

    expected_range: int = 1

    assert calculate_schedule_range(df) == expected_range


def test_calculate_schedule_range_empty_dataframe() -> None:
    """
    Test calculating the schedule range with an empty DataFrame.

    Asserts:
        Raises ValueError if the DataFrame is empty.
    """
    df: DataFrame = pd.DataFrame({"date": []})

    with pytest.raises(ValueError):
        calculate_schedule_range(df)


def test_calculate_schedule_range_invalid_dates() -> None:
    """
    Test calculating the schedule range with invalid date formats.

    Asserts:
        Raises ValueError if the dates are not in the expected format.
    """
    data: dict[str, list[str]] = {"date": ["2024-01-01", "2024-01-05"]}
    df: DataFrame = pd.DataFrame(data)

    with pytest.raises(ValueError):
        calculate_schedule_range(df)


if __name__ == "__main__":
    pytest.main([__file__])

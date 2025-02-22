from imports import *


def save_schedule_to_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the schedule DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame containing the schedule data with required columns:
            'course', 'lecturer', 'group', 'classroom', 'primary_color',
            'secondary_color', 'date', and 'time'.
        output_path (str): Path to save the CSV file.

    Raises:
        ValueError: If required columns are missing in the DataFrame.
        Exception: If any other error occurs during the file-saving process.
    """
    try:
        if not {
            "course",
            "lecturer",
            "group",
            "classroom",
            "primary_color",
            "secondary_color",
            "date",
            "time",
        }.issubset(df.columns):
            raise ValueError("Missing required columns")

        df = df.drop(["primary_color", "secondary_color"], axis=1)

        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"File successfully saved as: {output_path}")

    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
        raise


def calculate_schedule_range(df: pd.DataFrame) -> int:
    """
    Calculate the total range of the schedule in days.

    Args:
        df (pd.DataFrame): DataFrame containing the 'date' column with dates in 'dd.mm.yyyy' format.

    Returns:
        int: The total number of days covered by the schedule.

    Raises:
        ValueError: If the DataFrame is empty or if the 'date' column contains invalid values.
    """
    if df.empty:
        raise ValueError("The DataFrame is empty.")

    df["date"] = pd.to_datetime(df["date"], format="%d.%m.%Y")

    start_date = df["date"].min()
    end_date = df["date"].max()

    total_range: int = (end_date - start_date).days + 1
    print(f"Total schedule duration: {total_range} days")

    return total_range

from imports import *


def save_schedule_to_csv(df, output_path):
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


def calculate_schedule_range(df):
    if df.empty:
        raise ValueError("The DataFrame is empty.")

    df["date"] = pd.to_datetime(df["date"], format="%d.%m.%Y")

    start_date = df["date"].min()
    end_date = df["date"].max()

    total_range = (end_date - start_date).days + 1
    print(f"Total schedule duration: {total_range} days")

    return total_range


def save_results_to_file(filename, algorithm_name, schedule_range, computation_time):
    with open(filename, "a") as file:
        file.write(f"----------------------------------------------\n")
        file.write(f"Coloring algorithm: {algorithm_name}\n")
        file.write(f"Total schedule duration: {schedule_range} days\n")
        file.write(f"Computation time: {computation_time:.2f} s\n")

    print(f"Results saved in: {filename}")
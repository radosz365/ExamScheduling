import pandas as pd

def save_schedule_to_csv(df, output_path):

    df = df.drop(["primary_color", "secondary_color"], axis=1)

    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"File successfully saved as: {output_path}")

def calculate_schedule_range(df):

    df["date"] = pd.to_datetime(df["date"], format="%d.%m.%Y")

    start_date = df["date"].min()
    end_date = df["date"].max()

    total_range = (end_date - start_date).days + 1
    print(f"Total schedule duration: {total_range} days")
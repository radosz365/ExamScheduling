import pandas as pd
import random
import os


def unique_check(file_path):
    try:
        file = pd.read_csv(file_path)
        unique_rows = ~file.duplicated()
        return unique_rows.all()
    except Exception as e:
        print(f"Wystąpił błąd podczas próby odczytu pliku: {e}")
        return False


def generate_dataset(
    courses_path, lecturers_path, classrooms_path, groups_path, num_records
):
    courses = pd.read_csv(courses_path)
    lecturers = pd.read_csv(lecturers_path)
    classrooms = pd.read_csv(classrooms_path)
    groups = pd.read_csv(groups_path)

    courses_list = courses[courses.columns[0]].tolist()
    lecturers_list = lecturers[lecturers.columns[0]].tolist()
    classrooms_list = classrooms[classrooms.columns[0]].tolist()
    groups_list = groups[groups.columns[0]].tolist()

    max_combinations = (
        len(courses_list)
        * len(lecturers_list)
        * len(classrooms_list)
        * len(groups_list)
    )
    if num_records > max_combinations:
        raise ValueError(
            "Za dużo rekordów do wygenerowania. Zmniejsz liczbę wejściową."
        )

    records = set()
    while len(records) < num_records:
        record = (
            random.choice(courses_list),
            random.choice(lecturers_list),
            random.choice(groups_list),
            random.choice(classrooms_list),
        )
        records.add(record)

    os.makedirs("datasets", exist_ok=True)
    filename = f"datasets/dataset{num_records}.csv"
    while os.path.exists(filename):
        raise ValueError("Zestaw o takim rozmiarze już istnieje.")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("course,lecturer,group,classroom\n")
        for record in records:
            f.write(",".join(record) + "\n")

    return filename
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from imports import *

data_path: str = "datasets/dataset1000.csv"
database: List[Dict[str, Any]] = pd.read_csv(data_path).to_dict(orient="records")


class TestDatabase(unittest.TestCase):

    def test_unique_rows(self) -> None:
        rows: List[Tuple[Tuple[str, Any], ...]] = [tuple(row.items()) for row in database]
        self.assertEqual(len(rows), len(set(rows)), "Not all rows are unique.")

    def test_non_empty_values(self) -> None:
        for row in database:
            for key, value in row.items():
                self.assertIsNotNone(value, f"Missing value in column {key}")
                self.assertNotEqual(value, "", f"Empty value in column {key}")

    def test_course_format(self) -> None:
        for row in database:
            course: str = row["course"]
            self.assertIsInstance(course, str, "Course name should be a string")

    def test_lecturer_format(self) -> None:
        lecturer_pattern: re.Pattern = re.compile(
            r"^(Dr.?(?:\s+hab.?)?|Prof.|Mgr.|Inż.)\s+[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+(?:-[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+)?\s+[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+$"
        )
        for row in database:
            lecturer: str = row["lecturer"]
            self.assertRegex(
                lecturer, lecturer_pattern, "Incorrect lecturer name format"
            )

    def test_group_format(self) -> None:
        group_pattern: re.Pattern = re.compile(
            r"^[A-Z]{3}\.[A-Z]{2}[0-9]\.[A-Z]{3}\.[0-9]{4}\.[A-Z]{3}$"
        )
        for row in database:
            group: str = row["group"]
            self.assertRegex(group, group_pattern, "Incorrect group format")

    def test_classroom_format(self) -> None:
        classroom_pattern: re.Pattern = re.compile(r"^[A-Z][0-9]{3}$")
        for row in database:
            classroom: str = row["classroom"]
            self.assertRegex(classroom, classroom_pattern, "Incorrect classroom format")

if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

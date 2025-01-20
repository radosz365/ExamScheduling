import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from imports import *

data_path: str = "datasets/dataset1000.csv"
"""
Path to the input dataset CSV file.
"""

database: List[Dict[str, Any]] = pd.read_csv(data_path).to_dict(orient="records")
"""
List of dictionaries representing the dataset loaded from the CSV file.
"""


class TestDatabase(unittest.TestCase):
    """
    Unit tests for validating the structure and values in the dataset.
    """

    def test_unique_rows(self) -> None:
        """
        Ensure all rows in the dataset are unique.
        """
        rows: List[Tuple[Tuple[str, Any], ...]] = [
            tuple(row.items()) for row in database
        ]
        self.assertEqual(len(rows), len(set(rows)), "Not all rows are unique.")

    def test_non_empty_values(self) -> None:
        """
        Verify all values in the dataset are non-empty and not None.
        """
        for row in database:
            for key, value in row.items():
                self.assertIsNotNone(value, f"Missing value in column {key}")
                self.assertNotEqual(value, "", f"Empty value in column {key}")

    def test_course_format(self) -> None:
        """
        Check if the 'course' column contains valid strings.
        """
        for row in database:
            course: str = row["course"]
            self.assertIsInstance(course, str, "Course name should be a string")

    def test_lecturer_format(self) -> None:
        """
        Validate the format of the 'lecturer' column using a regex pattern.
        """
        lecturer_pattern: re.Pattern = re.compile(
            r"^(Dr.?(?:\s+hab.?)?|Prof.|Mgr.|Inż.)\s+[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+(?:-[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+)?\s+[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+$"
        )
        for row in database:
            lecturer: str = row["lecturer"]
            self.assertRegex(
                lecturer, lecturer_pattern, "Incorrect lecturer name format"
            )

    def test_group_format(self) -> None:
        """
        Ensure the 'group' column adheres to the expected format.
        """
        group_pattern: re.Pattern = re.compile(
            r"^[A-Z]{3}\.[A-Z]{2}[0-9]\.[A-Z]{3}\.[0-9]{4}\.[A-Z]{3}$"
        )
        for row in database:
            group: str = row["group"]
            self.assertRegex(group, group_pattern, "Incorrect group format")

    def test_classroom_format(self) -> None:
        """
        Verify the 'classroom' column follows the expected format.
        """
        classroom_pattern: re.Pattern = re.compile(r"^[A-Z][0-9]{3}$")
        for row in database:
            classroom: str = row["classroom"]
            self.assertRegex(classroom, classroom_pattern, "Incorrect classroom format")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

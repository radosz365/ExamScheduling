from main import create_schedule
from visualization_for_students import create_exam_schedule_png
from imports import *

dataset: str = "dataset1000.csv"
"""
The name of the dataset to be used for schedule creation.
"""

start_date: str = "30.01.2025"
"""
The starting date for the exam schedule.
"""

time_slots: List[str] = [
    "8:00-8:45",
    "9:00-9:45",
    "10:00-10:45",
    "11:00-11:45",
    "12:00-12:45",
    "13:00-13:45",
    "14:00-14:45",
    "15:00-15:45",
    "16:00-16:45",
]
"""
The list of available time slots for exams.
"""

create_schedule(dataset, start_date, time_slots)
"""
Generate the exam schedule using the specified dataset, start date, and time slots.
"""

file_path: str = "schedules/schedule_dataset1000.csv"
"""
The path to the generated schedule CSV file.
"""

group_to_display: str = "XGD.AR0.ANY.5116.CIL"
"""
The identifier of the group to visualize in the schedule.
"""

create_exam_schedule_png(file_path, group_to_display)
"""
Generate and save the visual representation of the schedule for the specified group.
"""

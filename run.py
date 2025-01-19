from main import create_schedule
from visualization_for_students import create_exam_schedule_png
from imports import *

# set the dataset
dataset = "dataset1000.csv"

# set the start date
start_date = "30.01.2025"

# set the time slots
time_slots = [
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

# call the create_schedule function
create_schedule(dataset, start_date, time_slots)

# set path to the schedule file
file_path = "schedules/schedule_dataset1000.csv"

# set the group to display
group_to_display = "XGD.AR0.ANY.5116.CIL"

# call the create_exam_schedule_png function to create the exam schedule
create_exam_schedule_png(file_path, group_to_display)


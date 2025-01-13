from dataset_generator_func import generate_dataset, unique_check

print(unique_check("resources/classrooms.csv"))
print(unique_check("resources/courses.csv"))
print(unique_check("resources/groups.csv"))
print(unique_check("resources/lecturers.csv"))


courses = "resources/courses.csv"
lecturers = "resources/lecturers.csv"
classrooms = "resources/classrooms.csv"
groups = "resources/groups.csv"

print(unique_check(generate_dataset(courses, lecturers, classrooms, groups, 200)))

# Dataset Documentation

## Overview

The dataset contains information about courses, lecturers, student groups, and classrooms. It serves as input for the scheduling algorithm that assigns exam times using graph coloring principles.

## Structure

The dataset is a CSV file with the following columns:

- **course**: The name of the course.  
  Example: "Budowanie marki online" (Building Online Brands).

- **lecturer**: The lecturer responsible for the course.  
  Example: "Dr. Anna Lewandowska".

- **group**: A unique code representing the group attending the course.  
  Example: "TNW.AG3.GVN.7332.DQB".

- **classroom**: The classroom where the course takes place.  
  Example: "H236".

## Example Data

Below is a sample of the dataset:

| Course                          | Lecturer                | Group                   | Classroom |
|---------------------------------|-------------------------|-------------------------|-----------|
| Międzynarodowe zarządzanie finansami | Dr. Anna Lewandowska   | TNW.AG3.GVN.7332.DQB    | H236      |
| Budowanie marki online          | Mgr. Tomasz Nowakiewicz | BFN.OF8.PWR.0279.RWQ    | E353      |
| Modelowanie finansowe           | Prof. Marek Wójcik      | OOG.CU9.LTX.5149.CYJ    | B135      |
| Tworzenie treści cyfrowych      | Dr hab. Katarzyna Kamińska | QSC.TR2.PPG.1283.PVD | H251      |
| Zarządzanie polem namiotowym    | Mgr. Jan Wiśniewski     | SZY.OR3.WYO.6406.MXZ    | H101      |

## Purpose

The data is used to identify scheduling conflicts and optimize exam timetables. The graph coloring algorithm processes this information to avoid clashes between student groups sharing the same lecturer or classroom.

## Usage Instructions

1. Ensure the dataset follows the format described above.
2. Provide the dataset as input to the scheduling program.
3. Run the graph coloring algorithm to generate conflict-free exam timetables.



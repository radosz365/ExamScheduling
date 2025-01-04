# Unit Tests

This section documents the unit tests for the program.
Include details about the testing framework, examples of test cases, and their purpose.


# Unit Tests

## Overview

Unit tests are designed to verify the functionality of individual components of the program. They ensure that each module performs as expected in isolation.

## Running Unit Tests

To execute the unit tests, run:
```bash
python -m unittest discover tests

Ensure that all tests pass before deploying or using the program to guarantee its reliability.

bash
Skopiuj kod

**6. `tests/val_tests.md` (Validation Tests):**

```markdown
# Validation Tests

## Purpose

Validation tests assess the performance of the scheduling algorithm using real-world datasets to ensure it meets the required criteria for efficiency and accuracy.

## Running Validation Tests

Execute the validation tests by running:
```bash
python validation_tests/run_validation.py
Review the output to confirm that the algorithm schedules exams correctly without conflicts.

vbnet
Skopiuj kod

**7. `data/data_ci_cd.md` (Data CI/CD):**

```markdown
# Data CI/CD

## Continuous Integration and Continuous Deployment

The project incorporates CI/CD practices to automate testing and deployment:

- **Continuous Integration (CI):** Automated testing is configured to run unit and validation tests on each commit to the repository.
- **Continuous Deployment (CD):** Upon successful tests, the latest version is deployed to the designated environment.

## Configuration

CI/CD is configured using GitHub Actions, with workflows defined in the `.github/workflows` director
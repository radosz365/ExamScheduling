## Workflow Overview

The workflow is triggered on events related to the `main` branch and ensures the application meets quality standards through unit tests, validation tests, and linting.

## Trigger Events

The workflow runs on the following events:

- **Push** events to the `main` branch.
- **Pull Requests** targeting the `main` branch.

## Permissions

The workflow grants `contents: read` permission for accessing the repository contents.

## Jobs

### Test and Lint Job

The `test-and-lint` job is responsible for running tests and performing linting. It runs on the latest Ubuntu environment.

### Steps

**1.Checkout the Repository**
```yaml
- uses: actions/checkout@v4
```
This step checks out the repository code to enable access to the application files.

**2.Set up Python Environment**
```yaml
- name: Set up Python 3.10
  uses: actions/setup-python@v3
  with:
    python-version: "3.10"
```
This step sets up a Python 3.10 environment.

**3.Install Dependencies**
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install flake8 pytest
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```
This step installs essential dependencies, including `flake8` for linting and `pytest` for testing. If a `requirements.txt` file exists, it installs the listed dependencies.

**4.Set Root Directory**
```yaml
- name: Set root
  run: echo "PYTHONPATH=$PWD" >> $GITHUB_ENV
```
This step ensures the root directory is correctly set for Python imports.

**5.Run Unit Tests**
```yaml
- name: Run unit tests
  run: |
    pytest unit_tests
```
This step runs unit tests located in the `unit_tests` directory.

**6.Run Validation Tests for Input File**
```yaml
- name: Run validation tests for input file
  run: |
    if [ -f validation_tests/test_input_file.py ]; then pytest validation_tests/test_input_file.py
    else echo "Input file does not exist. Skipping tests."; fi
```
This step conditionally runs input file validation tests if the test script exists.

**7.Run Validation Tests for Output File**
```yaml
- name: Run validation tests for output file
  run: |
    if [ -f validation_tests/test_output_file.py ]; then pytest validation_tests/test_output_file.py
    else echo "Output file does not exist. Skipping tests."; fi
```
This step conditionally runs output file validation tests if the test script exists.

**8.Linting with Super-Linter**
```yaml
- name: Linting with Super-Linter
  uses: github/super-linter@v5
  env:
    VALIDATE_PYTHON_PYLINT: true
    DEFAULT_BRANCH: main
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
This step performs linting using GitHub's Super-Linter, with `pylint` validation enabled for Python files.
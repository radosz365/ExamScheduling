# Usage

This section explains how to use the exam scheduling program.
Provide instructions and examples for users to understand its functionality.

# Usage Guide for the Exam Scheduling Application

This guide provides a step-by-step explanation for using the Exam Scheduling Application, aimed at users with no prior technical knowledge. Follow the instructions carefully to ensure successful operation of the application.

---

## Step 1: Install Python

Ensure Python is installed on your computer:
1. Go to the [Python website](https://www.python.org/).
2. Download the latest version of Python for your operating system.
3. Install Python by following the installation instructions.
4. Verify the installation by opening a terminal (Command Prompt/PowerShell on Windows, Terminal on macOS/Linux) and typing:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

---

## Step 2: Set Up the Project

### Clone the Repository
1. Download the project files or clone the repository containing the application.
   Example command to clone:
   ```bash
   git clone <repository_url>
   ```

### Navigate to the Project Folder
2. Open the terminal and navigate to the downloaded project folder:
   ```bash
   cd <project_folder>
   ```

---

## Step 3: Create a Virtual Environment

A virtual environment ensures that all dependencies are isolated to this project.

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.

---

## Step 4: Install Required Dependencies

The application uses external libraries that need to be installed:
1. Make sure you are inside the project folder.
2. Run the following command to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Step 5: Run the Application

1. Make sure the virtual environment is activated.
2. Execute the main script to start the application:
   ```bash
   python main.py
   ```

The application will load and provide outputs or visualizations based on your dataset and the implemented exam scheduling algorithm.

---

## Step 6: Use the Visualization Tool (Optional)

To generate visualizations for students:
1. Make sure the main script has been executed and the data has been processed.
2. Run the following command to execute the visualization tool:
   ```bash
   python visualization_for_students.py
   ```
3. Follow the on-screen instructions to generate visual outputs.

---

## Step 7: Exit the Virtual Environment

Once you're done, deactivate the virtual environment by typing:
```bash
deactivate
```

This will return your terminal to the global Python environment.

---

## Troubleshooting

### Common Issues:
1. **Python Command Not Found**: Ensure Python is properly installed and added to your system's PATH.
2. **Dependencies Not Installed**: Ensure the virtual environment is activated before running `pip install -r requirements.txt`.
3. **Script Errors**: Verify that you are in the correct project folder and that the dataset file paths are correct.

If issues persist, consult the application's documentation or contact the developer.

---

This guide is designed to help you use the Exam Scheduling Application effectively. Ensure you have the correct dataset files and follow the steps in order for best results.


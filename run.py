from main import create_schedule
from visualization_for_students import create_exam_schedule_png
from imports import *
from feature_flag import get_flag_value
from flask import Flask, request, render_template, jsonify
from visualization_for_students import create_exam_schedule_png
import os

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


enable_visualization = get_flag_value("api_enable", default_value=False)

if not enable_visualization:
    print("Flag is disabled. Generating schedule and visualization as code.")
    file_path = f"schedules/schedule_{dataset}"
    # call the create_schedule function
    print("Generating schedule...")
    create_schedule(dataset, start_date, time_slots)
    group_to_display = "XGD.AR0.ANY.5116.CIL"
    print(
        f"Visualization enabled. Generating visualization for group: {group_to_display}"
    )
    create_exam_schedule_png(file_path, group_to_display)
else:
    app = Flask(__name__, static_folder="visualizations")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/show_schedule", methods=["GET"])
    def show_schedule():
        group = request.args.get("group")
        file_name = request.args.get("file_name")
        file_path = f"schedules/schedule_{file_name}"

        if not group or not file_path:
            return (
                jsonify(
                    {"error": "Both 'group' and 'file_path' parameters are required"}
                ),
                400,
            )

        if not os.path.exists(file_path):
            return jsonify({"error": f"File not found: {file_path}"}), 404

        try:
            create_exam_schedule_png(file_path, group)
            output_path = f"visualizations/{group.replace('.', '_')}.png"
            return render_template("show_schedule.html", image_path=output_path)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    if __name__ == "__main__":
        app.run(debug=True)

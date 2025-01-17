from flask import Flask, request, render_template, abort
from visualization_for_students import create_exam_schedule_png
import os

app = Flask(__name__, static_folder="visualizations")


@app.route("/", methods=["GET"])
def hello():
    return render_template("index.html")


@app.route("/show_schedule", methods=["GET"])
def show_schedule():
    group = request.args.get("group")
    file_path = request.args.get("file_path")

    # Walidacja parametrów
    if not group:
        return "Group parameter is required", 400
    if not file_path:
        return "File path parameter is required", 400

    group = group.upper()

    # Sprawdzenie, czy plik istnieje
    if not os.path.exists(file_path):
        return f"File not found: {file_path}", 404

    try:
        create_exam_schedule_png(file_path, group)
    except Exception as e:
        return f"An error occurred: {e}", 500

    output_path = f"visualizations/{group.replace('.', '_')}.png"
    return render_template("show_schedule.html", image_path=output_path)


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, request, render_template
from main import create_exam_schedule_png_for_students


app = Flask(__name__, static_folder="visualizations")


@app.route("/home", methods=["GET"])
def hello():
    return render_template("home.html")


@app.route("/show_schedule", methods=["GET"])
def show_schedule():
    group = request.args.get("group").upper()
    create_exam_schedule_png_for_students(group)
    output_path = f"visualizations/{group.replace('.', '_')}.png"
    return render_template("show_schedule.html", image_path=output_path)


if __name__ == "__main__":
    app.run(debug=True)

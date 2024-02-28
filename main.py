from flask import Flask, render_template, request
from scripts.Structures import Todo

app = Flask(__name__)
user_tasks = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["get", "post"])
def tasks():
    if request.method == "POST":
        user_tasks.append(Todo(request.form["title"], request.form["details"], request.form["deadline"]))
        print(user_tasks)
    
    return render_template("taskPage.html")

@app.route("/studycontrol")
def studycontrol():
    return render_template("studyControl.html")

if __name__ == "__main__":
    app.run(debug=True)

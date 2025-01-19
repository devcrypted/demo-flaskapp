from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# This will serve as our "database" for tasks
tasks = []


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/task", methods=["POST"])
def create_task():
    task_title = request.form.get("task_title")
    if task_title:
        tasks.append({"id": len(tasks) + 1, "title": task_title})
    return redirect("/")


@app.route("/task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"success": True})


@app.route("/task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task_title = request.form.get("task_title")
    if task_title:
        for task in tasks:
            if task["id"] == task_id:
                task["title"] = task_title
                break
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template_string, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
db = SQLAlchemy()

# Define a database model named Task for storing task data
class Task(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    description: Mapped[str] = mapped_column(db.String(256), nullable=False)

# Initialize SQLAlchemy with the configured Flask application
db.init_app(app)

# Initialize the database within the application context
with app.app_context():
    db.create_all()  # Creates all tables

# HTML template with inline CSS for the webpage, includes form for adding tasks and lists existing tasks with delete option
HOME_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>To-Do List</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      margin: 40px auto;
      padding: 20px;
      max-width: 600px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h1 {
      color: #333;
    }
    form {
      margin-bottom: 20px;
    }
    input[type="text"] {
      padding: 10px;
      width: calc(100% - 22px);
      margin-bottom: 10px;
    }
    input[type="submit"] {
      background-color: #5cb85c;
      border: none;
      color: white;
      padding: 10px 20px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      cursor: pointer;
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      position: relative;
      padding: 8px;
      background-color: #fff;
      border-bottom: 1px solid #ddd;
    }
    .delete-button {
      position: absolute;
      right: 10px;
      top: 10px;
      background-color: #ff6347;
      color: white;
      border: none;
      padding: 5px 10px;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>To-Do List</h1>
  <form action="/add" method="post">
    <input type="text" name="task" placeholder="Add new task">
    <input type="submit" value="Add Task">
  </form>
  <ul>
    {% for task in tasks %}
      <li>{{ task.description }} <button class="delete-button" onclick="location.href='/delete/{{ task.id }}'">Delete</button></li>
    {% endfor %}
  </ul>
</body>
</html>
"""

# Define route for the home page to display tasks
@app.route("/", methods=["GET"])
def home():
    tasks = Task.query.all()  # Retrieve all tasks from the database
    return render_template_string(
        HOME_HTML, tasks=tasks
    )  # Render the homepage with tasks listed

# Define route to add new tasks from the form submission
@app.route("/add", methods=["POST"])
def add():
    task_description = request.form["task"]  # Extract task description from form data
    new_task = Task(description=task_description)  # Create new Task instance
    db.session.add(new_task)  # Add new task to database session
    db.session.commit()  # Commit changes to the database
    return redirect(url_for("home"))  # Redirect to the home page

# Define route to delete tasks based on task ID
@app.route("/delete/<int:task_id>", methods=["GET"])
def delete(task_id: int):
    task_to_delete = Task.query.get(task_id)  # Get task by ID
    if task_to_delete:
        db.session.delete(task_to_delete)  # Remove task from the database session
        db.session.commit()  # Commit the change to the database
    return redirect(url_for("home"))  # Redirect to the home page

# Check if the script is the main program and run the app
if __name__ == "__main__":
    app.run()  # Start the Flask application
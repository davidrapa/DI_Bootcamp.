# from flask import render_template, redirect, url_for
# from todo_app import app
# from todo_app.forms import AddTodoForm
# from todo_app.models import Todo
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = AddTodoForm()
#     if form.validate_on_submit():
#         new_task = Todo(details=form.task.data)
#         new_task.save_task_to_db()
#         return redirect(url_for('index'))
#     tasks = Todo.query.all()
#     return render_template('index.html', form=form, tasks=tasks)

# part 3

from flask import render_template, redirect, url_for
from todo_app import create_app
from todo_app.forms import AddTodoForm
from todo_app.models import Todo
from todo_app.extensions import db

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddTodoForm()
    if form.validate_on_submit():
        task = Todo(details=form.task.data)
        task.save_task_to_db()
        return redirect(url_for('index'))
    tasks = Todo.query.all()
    return render_template('index.html', form=form, tasks=tasks)

@app.route('/complete/<int:todo_id>', methods=['POST'])
def complete_task(todo_id):
    task = Todo.query.get_or_404(todo_id)
    task.set_task_as_complete()
    return redirect(url_for('index'))

# why you ahve views and routes?
from todo_app.extensions import db
from todo_app.models import Todo
from todo_app.forms import AddTodoForm
from flask import render_template, redirect, url_for

def register_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = AddTodoForm()
        if form.validate_on_submit():
            new_task = Todo(details=form.task.data)
            new_task.save_task_to_db()
            return redirect(url_for('index'))
        tasks = Todo.query.all()
        return render_template('index.html', form=form, tasks=tasks)

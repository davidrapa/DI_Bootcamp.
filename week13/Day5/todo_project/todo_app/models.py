# from todo_project import db
#
# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     details = db.Column(db.Text, nullable=False)
#
#     def save_task_to_db(self):
#         db.session.add(self)
#         db.session.commit()

# part 3

from todo_app.extensions import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()

    def set_task_as_complete(self):
        self.completed = True
        db.session.commit()


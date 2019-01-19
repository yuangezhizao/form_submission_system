from flask import Blueprint, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from main.models.todos import TODO

todos_bp = Blueprint('todos', __name__)


class Form(FlaskForm):
    details = StringField()
    submit = SubmitField()


@todos_bp.route('/')
def index():
    todos = TODO.query.all()
    return render_template('main/todos.html', todos=todos)


@todos_bp.route('/todos', methods=['POST'])
def add():
    form = Form()
    if form.validate_on_submit():
        details = form.details.data
        count = TODO.query.count()
        todo = TODO(id=count + 1, details=details)
        todo.save()
    return redirect(url_for('todos.index'))

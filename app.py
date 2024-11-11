import sqlite3

from flask import (
    Flask,
    render_template,
    request,
    redirect
)

from config import config

from models.langs import LangsModel
from models.users import UsersModel
from models.todos import TodosModel

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        'home.html',
        todos = TodosModel.get_data()
    )

@app.route("/make_todo", methods=['POST'])
def make_todo():
    if 'make_todo' in request.form:
        TodosModel.add_data({
            'todo': request.form['make_todo']
        })
        return redirect('/')

@app.route("/update_todo/<int:id>", methods=['POST', 'GET'])
def update_todo(id):
    if request.method == 'POST':
        TodosModel.update_data({
            'todo': request.form['update_todo']
        }, id)
        return redirect('/')
    if request.method == 'GET':
        return render_template(
            'update.html',
            todo = TodosModel.get_data_by_pk(id)
        )
    
@app.route("/delete_todo/<int:id>")
def delete_todo(id):
    TodosModel.delete_data(f'"todo_id" = { id }')
    return redirect('/')

@app.route("/delete_all")
def delete_all():
    TodosModel.delete_data()
    return redirect('/')


if __name__ == '__main__':
    app.run(
        debug = True,
        port = 80
    )

# print(TodosModel.get_data())

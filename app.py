import sqlite3

from flask import *

from models.todos import TodosModel

from controllers.home import home
from controllers.api import api
from controllers.about import about
from controllers.contact import contact

from controllers.dashboard.home import dashboard_home
from controllers.dashboard.update import dashboard_update

app = Flask(__name__, template_folder='views')

# Main pages
home.register_blueprint(contact, url_prefix='/Contact')
home.register_blueprint(about, url_prefix='/About')
home.register_blueprint(api, url_prefix='/API')
app.register_blueprint(home, url_prefix="/<string:lang>")

# Dashboard
dashboard_home.register_blueprint(dashboard_update, url_prefix='/Update')
app.register_blueprint(dashboard_home, url_prefix='/Dashboard')


@app.route("/")
def home_page():
    return redirect('/AR')

#############################################################

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

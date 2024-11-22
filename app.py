import sqlite3

from flask import *

from models.todos import TodosModel

from controllers.home import home
from controllers.api import api
from controllers.about import about
from controllers.contact import contact
from controllers.update import update_todo

from controllers.dashboard.home import dashboard_home
from controllers.dashboard.update import dashboard_update

app = Flask(__name__, template_folder='views')

# Main 
home.register_blueprint(contact, url_prefix='/Contact')
home.register_blueprint(about, url_prefix='/About')
home.register_blueprint(api, url_prefix='/API')
app.register_blueprint(home, url_prefix="/<string:lang>")

app.register_blueprint(update_todo)

# Dashboard
dashboard_home.register_blueprint(dashboard_update, url_prefix='/Update')
app.register_blueprint(dashboard_home, url_prefix='/Dashboard')


@app.route("/")
def home_page():
    return redirect('/AR')

@app.errorhandler(404)
@app.errorhandler(405)
def not_found(e):
    return f"<h1>ERROR: { str(e)[:3] } page</h1>", 404

#############################################################

@app.route("/make_todo", methods=['POST'])
def make_todo():
    if ('make_todo' in request.form
        and 'user_id' in request.form):
        TodosModel.add_data({
            'todo': request.form['make_todo'],
            'user_id': int(request.form['user_id'])
        })
        return redirect('/')
    return 'Not pass'


@app.route("/delete_all/<int:user_id>")
def delete_all(user_id):
    TodosModel.delete_data('"user_id" = '+ user_id)
    return redirect('/')


if __name__ == '__main__':
    app.run(
        debug = True,
        port = 80
    )

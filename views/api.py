from flask import Blueprint, render_template, abort

from config import vars
from models.todos import TodosModel

api = Blueprint('api', __name__)

@api.route("/")
def api_page(lang):
    if lang in vars.list_langs:
        return "just a test"
    abort(404)

from flask import Blueprint, render_template, abort, redirect, request

from config import vars
from models.langs import LangsModel
from models.todos import TodosModel
from models.site_words import SiteWordsModel
from models.users import UsersModel

words = {}
language = LangsModel.get_data()

if bool(language):
    for langu in language:
        # words[langu['lang_short']] = langu['lang_short']
        
        words_in_lang = SiteWordsModel.get_data(
            '"lang_id" = '+ str(langu['lang_id'])
        )
        lang_kies = {}
        for word_key in words_in_lang:
            lang_kies[word_key['word_key']] = SiteWordsModel.get_by_key(
                word_key['word_key'],
                langu['lang_id']
            )
        words[langu['lang_short']] = lang_kies

api = Blueprint('api', __name__)

@api.route('/', methods=['POST'])
def api_page(lang):
    if lang in vars.list_langs:
        if request.method == 'POST':
            if 'update_todo' in request.form:
                TodosModel.update_data({
                    'todo': request.form['update_todo']
                }, id)
                return redirect('/')
            # Singup
            if ('signup_username' in request.form
                and 'signup_password' in request.form
                and 'signup_repassword' in request.form):
                if request.form['signup_password'] == request.form['signup_repassword']:
                    UsersModel.add_data({
                        'username': request.form['signup_username'],
                        'password': request.form['signup_password']
                    })
                    # login
                return redirect('/')
            # Singin
            if ('signin_username' in request.form
                and 'signin_password' in request.form):
                users = UsersModel.get_data()
                logedin = False
                for user in users:
                    if (request.form['signin_username'] == user['username']
                        and request.form['signin_password'] == user['password']):
                        logedin = True
                        return 'logined'
                if not logedin:
                    return render_template(
                        'home.html',
                        todos = TodosModel.get_data(),
                        lang = lang,
                        words = words,
                        un = request.form['signin_username'],
                        ps = request.form['signin_password'],
                        err = 'bad values'
                    )
                    
    abort(404)

from flask import Blueprint, render_template, abort, request

from config import vars
from models.langs import LangsModel
from models.todos import TodosModel
from models.site_words import SiteWordsModel

home = Blueprint('home', __name__)

words = {}
language = LangsModel.get_data()

# {
#     'AR': {
#         'id': 'م',
#         'val': 'بيان',
#         'btns': 'ازرار',
#     },
#     'EN': {
#         'id': 'id',
#         'val': 'value',
#         'btns': 'btns',
#     }
# }

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

@home.route("/")
def home_page_by_lang(lang):
    if lang in vars.list_langs:
        
        try:
            cookie = request.cookies.get('LOGIN')
        except:
            cookie = False

        return render_template(
            'home.html',
            todos = TodosModel.get_data(),
            lang = lang,
            words = words,
            un = '',
            ps = '',
            err = '',
            cookie = cookie,
            url = request.url
        )
    abort(404)

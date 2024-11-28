from flask import Blueprint, render_template, abort, request
from models.users import UsersModel
from models.profile import UserProfileModel
from lib.encrypt import DataEncrypt

# phone number
from models.phone_number import PhoneNumberModel

profile = Blueprint('profile', __name__)

@profile.route('/<string:username>/')
def profile_page(lang, username):

    users = UsersModel.get_data()
    for user in users:
        cookie = request.cookies.get('LOGIN')
        cookie = DataEncrypt.decrypt(cookie)

        if username == user['username']:
            return render_template(
                'profile.html',
                username = username,
                lang = lang,
                user = UserProfileModel.get_data_by_pk(user['user_id']),
                iam = True if cookie == username else False,
                phones = PhoneNumberModel.get_data(
                    '"user_id" = '+ str(user['user_id'])
                )
            )
    abort(404)

from lib.encrypt import DataEncrypt
from models.users import UsersModel


# data = str({"id": 1, "first_name": "مينا"})
# data = "Mena مينا"

# enc = DataEncrypt.encrypt(data)
# print(enc)

# print(DataEncrypt.decrypt(enc))

# print(type(DataEncrypt.decrypt(enc, 'obj')))
# print(type(DataEncrypt.decrypt(enc)))

# print(str(UsersModel.add_data({
#     'username': 'Mon',
#     'password': DataEncrypt.encrypt('1234')
# })))

# user = UsersModel.get_data_by_pk(2)

# print(DataEncrypt.decrypt(user['password']))

from datetime import datetime, timedelta
import pytz
from flask import make_response

# print(type(datetime.now(pytz.timezone('Africa/Cairo'))))

# print(datetime(2024, 6, 10, 14, 30, 2, 100, tzinfo=pytz.timezone('Africa/Cairo')))

# print(timedelta(minutes = 1))
# print(timedelta(hours = 1))
# print(timedelta(days = 1))
# print(timedelta(days = 1, hours = 2))
# print(timedelta(days = 1, hours = 2, minutes = 2))
# print(timedelta(days = 1, hours = 2, minutes = 2, milliseconds = 2))
# print(timedelta(days = 1, hours = 2, minutes = 2, seconds = 2, milliseconds = 2))

# print((datetime(
#     2024, 6, 10, 14, 30, 2, 100,
#     tzinfo=pytz.timezone('Europe/Warsaw')
# )))

now = datetime.now(pytz.timezone('Africa/Cairo'))
after = timedelta(days = 10 * 365)

print(now + after)



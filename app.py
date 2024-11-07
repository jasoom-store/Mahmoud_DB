from config import config
from db.sqlite_db import SQLITE_DB
from abs.model import Model

from models.langs import LangsModel
from models.users import UsersModel

SQL = SQLITE_DB({
    "path": config.database_path
})

print('=' * 30)

print(UsersModel.create_table())

# print(LangsModel.delete_table())
# print(LangsModel.create_table())
# print(LangsModel.add_data({
#     # 'lang_id': 1,
#     'lang_name': 'Arabic',
# }))

# print(LangsModel.add_data({
#     'lang_id': 3,
#     'lang_name': 'Frensh',
# }))

# print(LangsModel.add_data({
#     'lang_id': 2,
#     'lang_name': 'English',
# }))

# print(LangsModel.update_data({
#     'lang_name': 'Englishaaaaaaaa',
# }, 2))

# print(LangsModel.delete_data('"lang_name" = "Arabic"'))

# print(LangsModel.get_data())
print(LangsModel.get_last_pk())

# class users(Model):
#   table_name = 'users'
#   pk = 'user_id'
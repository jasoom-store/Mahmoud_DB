from config import config
from db.sqlite_db import SQLITE_DB
from abs.model import Model

SQL = SQLITE_DB({
    "path": config.database_path
})

print('=' * 30)

# print(SQL.delete_table('langs'))

# print(SQL.create_table('langs', [
#     {
#         'n': 'lang_id',
#         't': 'INTEGER',
#         'l': False,
#         'pk': True,
#         'au': True
#     },
#     {
#         'n': 'lang_name',
#         't': 'TEXT',
#         'l': False,
#         'pk': False,
#         'au': False
#     },
# ]))

# print(SQL.add_data('langs', {
#     # 'lang_id': 1,
#     'lang_name': 'Arabic',
# }))

# print(SQL.add_data('langs', {
#     'lang_id': 3,
#     'lang_name': 'Frensh',
# }))

# print(SQL.add_data('langs', {
#     'lang_id': 2,
#     'lang_name': 'English',
# }))

# print(SQL.update_data('langs', {
#     'lang_name': 'English',
# }, 'lang_id', 2))

# print(SQL.get_data('langs'))

# print(SQL.get_data_by_pk('langs', 'lang_id', 1))


class langs(Model):
  table_name = 'langs'
  pk = 'lang_id'
  columes = [
    {
      'n': 'lang_id',
      't': 'INTEGER',
      'l': False,
      'pk': True,
      'au': True
    },
    {
      'n': 'lang_name',
      't': 'TEXT',
      'l': False,
      'pk': False,
      'au': False
    },
  ]

# print(langs.delete_table())
# print(langs.create_table())
# print(langs.add_data({
#     # 'lang_id': 1,
#     'lang_name': 'Arabic',
# }))

# print(langs.add_data({
#     'lang_id': 3,
#     'lang_name': 'Frensh',
# }))

# print(langs.add_data({
#     'lang_id': 2,
#     'lang_name': 'English',
# }))

# print(langs.update_data({
#     'lang_name': 'Englishaaaaaaaa',
# }, 2))

# print(langs.delete_data('"lang_name" = "Arabic"'))

# print(langs.get_data())
print(langs.get_last_pk())

# class users(Model):
#   table_name = 'users'
#   pk = 'user_id'
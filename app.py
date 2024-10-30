from config import config
from db.sqlite_db import SQLITE_DB

SQL = SQLITE_DB({
    "path": config.database_path
})

print('=' * 30)

print(SQL.delete_table('langs'))

print(SQL.create_table('langs', [
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
]))

print(SQL.add_data('langs', {
    # 'lang_id': 1,
    'lang_name': 'Arabic',
}))

print(SQL.add_data('langs', {
    'lang_id': 3,
    'lang_name': 'Frensh',
}))

print(SQL.add_data('langs', {
    'lang_id': 2,
    'lang_name': 'English',
}))

from abs.model import Model

class UsersModel(Model):
  table_name = 'users'
  pk = 'user_id'
  columes = [
    {
      'n': 'user_id',
      't': 'INTEGER',
      'l': False,
      'pk': True,
      'au': True
    },
    {
      'n': 'username',
      't': 'TEXT',
      'l': False,
      'pk': False,
      'au': False
    },
    {
      'n': 'password',
      't': 'TEXT',
      'l': False,
      'pk': False,
      'au': False
    },
  ]
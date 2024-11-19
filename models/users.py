from abs.model import Model
from config import hex

class UsersModel(Model):
  table_name = f'{hex.hex_tables}_users'
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
      'l': False
    },
    {
      'n': 'password',
      't': 'TEXT',
      'l': False
    },
  ]
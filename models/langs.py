import __init__
from abs.model import Model

class LangsModel(Model):
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
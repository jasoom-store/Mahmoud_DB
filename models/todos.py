import __init__
from abs.model import Model

class TodosModel(Model):
  table_name = 'hex_todo'
  pk = 'todo_id'
  columes = [
    {
      'n': 'todo_id',
      't': 'INTEGER',
      'l': False,
      'pk': True,
      'au': True
    },
    {
      'n': 'todo',
      't': 'TEXT',
      'l': False
    }
  ]

  
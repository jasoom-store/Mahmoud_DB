from abs.model import Model

class SiteWordsModel(Model):
  table_name = 'site_words'
  pk = 'word_id'
  columes = [
    {
      'n': 'word_id',
      't': 'INTEGER',
      'l': False,
      'pk': True,
      'au': True
    },
    {
      'n': 'word_key',
      't': 'TEXT',
      'l': False,
      'pk': False,
      'au': False
    },
    {
      'n': 'word',
      't': 'TEXT',
      'l': False,
      'pk': False,
      'au': False
    },
    {
      'n': 'lang_id',
      't': 'INTEGER',
      'l': False,
      'pk': False,
      'au': False
    },
  ]

  @classmethod
  def get_by_key(cls, key : str, lang: int):
    try:
        res = cls.con.get_data(
            cls.table_name,
            f'"word_key" = "{key}" AND "lang_id" = {str(lang)}'
        )
        return res[0]['word']
    except:
        return False

  
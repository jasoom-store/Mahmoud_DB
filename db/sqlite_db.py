import sqlite3

class SQLITE_DB:
    def __init__(self, database : dict):
        self.__con = sqlite3.connect(database["path"])
        self.__cur = self.__con.cursor()

    # HERE AN ERROR
    def commit(self):
        return self.commit()

    # HERE AN ERROR
    def commit_and_close(self):
        self.commit()
        return self.close()

    def table_exists(self, table_name : str):
        sql = 'SELECT name FROM sqlite_master WHERE '
        sql += f'type="table" AND name="{ table_name }"'
        
        table_exists = self.__cur.execute(sql)
        tuple_data = table_exists.fetchone()

        if type(tuple_data) == tuple and table_name in tuple_data:
            return True
        return False

    def create_table(self, table_name : str, columes : list):
        try:
            # primary_key = False
            # auto_inc = False

            sql = f'CREATE TABLE "{ table_name }" ('
            for colume in columes:
                sql += '"'+ colume["n"] +'" '+ colume["t"]
                sql += ' NULL' if colume["l"] else ' NOT NULL'
                sql += ' PRIMARY KEY' if colume["pk"] else ''
                sql += ' AUTOINCREMENT' if colume["au"] else ''
                sql += ', '
                # if colume['pk']:
                #     primary_key = colume["n"]
                #     auto_inc = colume['au']

            # if type(primary_key) == str:
            #     sql += f' PRIMARY KEY("{ primary_key }"'
            #     if auto_inc:
            #         sql += ', AUTOINCREMENT'
            #     sql += '), '

            sql = sql[:-2]
            sql += ')'

            self.__cur.execute(sql)

            return self.table_exists(table_name)
        except:
            return 'This table is exists.'

    def delete_table(self, table_name : str):
        try:
            self.__cur.execute(f'DROP TABLE { table_name }')
            if not self.table_exists(table_name):
                return True
            return False
        except:
            return 'This table isn\'t exists.'
    
    def delete_data(self, table_name : str, where = '' : str):
        if self.table_exists(table_name):
            sql = f'DELETE FROM TABLE { table_name }'
            sql += f' WHERE { where }' if len(where) > 0 else ''
            self.__cur.execute(sql)
            return True
        return False

    def add_data(self, table_name : str, data : dict):
        sql = f'INSERT INTO "{ table_name }" ('
        for colume in data:
            if type(data[colume]) == str or type(data[colume]) == int:
                sql += '`'+ colume +'`, '
        sql = sql[:-2]
        sql += ') VALUES ('
        for colume in data:
            if type(data[colume]) == str:
                sql += f"'{ data[colume] }', "
            elif type(data[colume]) == int:
                sql += f'{ str(data[colume]) }, '
        sql = sql[:-2]
        sql += ')'

        self.__cur.execute(sql)
        self.__con.commit()


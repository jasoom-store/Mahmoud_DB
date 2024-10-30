import sqlite3


class SQLITE_DB:
    def __init__(self, database : dict):
        self.__con = sqlite3.connect(database["path"])
        self.__cur = self.__con.cursor()

    def commit(self):
        return self.commit()

    def commit_and_close(self):
        self.commit()
        return self.close()

    def table_exists(self, table_name):
        table_exists = self.__cur.execute(
            f'SELECT name FROM sqlite_master WHERE type="table" AND name="{ table_name }"'
        )

        tuple_data = table_exists.fetchone()

        if type(tuple_data) == tuple:
            if table_name in tuple_data:
                return True
        return False  

    def create_table(self, table_name, columes : list):
        try:
            # primary_key = False
            # auto_inc = False

            sql = f'CREATE TABLE "{ table_name }" ('
            for colume in columes:
                sql += '"'+ colume["n"] +'" '+ colume["t"]
                sql += ' NULL' if colume["l"] else ' NOT NULL'
                sql += '  PRIMARY KEY' if colume["pk"] else ''
                sql += '  AUTOINCREMENT' if colume["au"] else ''
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

    def delete_table(self, table_name):
        try:
            self.__cur.execute(f'DROP TABLE { table_name }')
            if not self.table_exists(table_name):
                return True
            return False
        except:
            return 'This table is not exists.'
    
    def delete_all_data(self, table_name):
        if self.table_exists(table_name):
            self.__cur.execute(f'DELETE FROM TABLE { table_name }')
            return True
        return False

    # INSERT INTO 'langs' ('lang_id', 'lang_name') VALUES (1, 'Arabic')
    def add_data(self, table_name, data : dict):
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
        
        # return sql




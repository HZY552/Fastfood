import sqlite3 as sql


class database:
    

    def __init__(self): 
        self.path_database = "C://Users//pc//OneDrive//桌面//tp/resto.db"
        # self.conn = None
        try:
            self.conn = sql.connect(self.path_database)
        except sql.Error as e:
            self.database_error = e

    def select_all(self,table):
        print(self.conn)
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM " + table)
        rows = cur.fetchall()
        cur.close()
        return rows

    def select_with_id(self,table,id,id_column,result):
        cur = self.conn.cursor()
        cur.execute("SELECT " + str(result) + " FROM " + table + " WHERE " + str(id_column) + "=" + str(id))
        rows = cur.fetchall()
        return rows

    def show_all_database(self):
        cur = self.conn.cursor()
        cur.execute("SELECT name FROM sqlite_sequence")
        res = cur.fetchone()  
        cur.close()
        return res     

    def insert_table_once(self,table,list_value):
        cur = self.conn.cursor()
        # cur.execute("INSERT INTO " + table + " (?,?) VALUES ") pas bon!!!
        cur.execute("INSERT INTO " + table + " VALUES(?,?)",list_value)
        self.conn.commit()
        cur.close()

    def update_once_withID(self,table,id,nom_column,value,column_id):
        cur = self.conn.cursor()
        cur.execute("UPDATE " + table + " SET " + str(nom_column) + " = " + str(value) + " WHERE " + str(column_id) + " = " + str(id))
        self.conn.commit()
        cur.close()

    

              

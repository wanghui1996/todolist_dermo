import sqlite3


class TodoDB():
    def  __init__(self):
        self.conn = sqlite3.connect('test.db')
    def cursor(self):
        return self.conn.cursor()
    def close(self):
        self.conn.close()
    def commit(self):
        self.conn.commit()




    def read_all(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('select id, content from todo order by id desc')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        # data = [d[0] for d in data]
        return data

    def read(self, todo_id):
        cursor = self.cursor()
        cursor = cursor.execute('select id, content from todo where id=?', (todo_id,))
        data = cursor.fetchone()
        cursor.close()
        return  data


    def init_db(self):

        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        # cursor.execute ("drop table if exists todo")
        # cursor.execute("create table todo (id integer primary key AUTOINCREMENT, content varchar(50))")
        cursor.close()
        conn.commit()
        conn.close()

    def test(self):
        pass

    def delete(self, todo_id):
        cursor = self.cursor()
        cursor = cursor.execute('delete from todo where id=?', (todo_id, ))
        cursor.close()
        self.commit()
        return
        print('delete', todo_id)

    def create(self, text):
        cursor = self.cursor()
        cursor = cursor.execute('insert into todo(content) values (?)', (text, ))
        cursor.close()
        self.commit()



if __name__ =='__main__':
    db = TodoDB()
    db.init_db()
    a = db.read_all()
    print(a)
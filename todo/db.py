import sqlite3


class TodoDB():
    def read_all(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('select id, content from todo')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        # data = [d[0] for d in data]
        return data

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
        print('delete', todo_id)


if __name__ =='__main__':
    db = TodoDB()
    db.init_db()
    a = db.read_all()
    print(a)
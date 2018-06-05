import sqlite3


class TodoDB():
    def __init__(self):
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
        cursor.execute('select id, content, status from todo order by id desc')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        # data = [d[0] for d in data]
        return data

    def read(self, todo_id):
        cursor = self.cursor()
        cursor = cursor.execute('select id, content, status from todo where id=?', (todo_id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def init_db(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        # cursor.execute ("drop table if exists todo")
        cursor.execute("create table if not exists todo (id integer primary key AUTOINCREMENT, content varchar(50))")
        cursor.close()
        conn.commit()
        conn.close()

    def migrate_latest(self):
        # 数据库迁移
        self.init_db()
        self.s2_add_status_column()

    # def test(self):
    #     pass

    def delete(self, todo_id):
        cursor = self.cursor()
        cursor = cursor.execute('delete from todo where id=?', (todo_id,))
        cursor.close()
        self.commit()
        return
        # print('delete', todo_id)

    def create(self, text):
        cursor = self.cursor()
        cursor = cursor.execute('insert into todo(content) values (?)', (text,))
        cursor.close()
        self.commit()


    def s2_add_status_column(self):
        conn = sqlite3.connect('test.db')
        cursor = self.cursor()
        # cursor.execute("drop table if exists todo")
        cursor.execute("alter table todo add column status varchar default 'done'")
        cursor.close()
        conn.commit()
        conn.close()


    def update_status(self, todo_id, status):
        cursor = self.cursor()
        cursor = cursor.execute('update todo set status = ? where id =?', (status, todo_id))
        self.commit()
        data = cursor.fetchone()
        print(data)
        cursor.close()
        return data


if __name__ == "__main__":
    db = TodoDB()
    # db.init_db()
    # a = db.read_all()
    db.migrate_latest()
    # print(a)

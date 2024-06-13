import sqlite3

conn = sqlite3.connect('blog.db')
c = conn.cursor()
c.execute('''
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
''')
conn.commit()
conn.close()

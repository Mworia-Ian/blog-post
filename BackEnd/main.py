from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Post(BaseModel):
    id: int
    title: str
    content: str

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/posts")
def read_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return posts

@app.post("/posts")
def create_post(post: Post):
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                 (post.title, post.content))
    conn.commit()
    conn.close()
    return post

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    conn = get_db_connection()
    conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?',
                 (post.title, post.content, post_id))
    conn.commit()
    conn.close()
    return post

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    return {"message": "Post deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from config import db
from sqlalchemy import text

from entities.todo import Todo

def get_todos():
    result = db.session.execute(text("SELECT id, title, author, year, publisher FROM Books"))
    todos = result.fetchall()
    return [Todo(todo[0], todo[1], todo[2], todo[3], todo[4]) for todo in todos]

def create_todo(key, title, author, year, publisher, address):
    sql = text("INSERT INTO Books (key, title, author, year, publisher, address) VALUES (:title, :author, :year, :publisher)")
    db.session.execute(sql, {"key": key, "title": title, "author": author, "year": year, "publisher": publisher, "address": address })
    db.session.commit()

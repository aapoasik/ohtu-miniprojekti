from config import db
from sqlalchemy import text
from entities.article import Article
from entities.todo import Todo

def get_todos():
    result = db.session.execute(text("""
        SELECT id, key, title, author, year, publisher, address
        FROM Books
    """))

    todos = result.fetchall()

    return [
        Todo(
            todo[0], todo[1], todo[2], todo[3],
            todo[4], todo[5], todo[6]
        )
        for todo in todos
    ]

def create_todo(key, title, author, year, publisher, address):
    sql = text("""
        INSERT INTO Books (key, title, author, year, publisher, address)
        VALUES (:key, :title, :author, :year, :publisher, :address)
    """)

    db.session.execute(sql, {
        "key": key,
        "title": title,
        "author": author,
        "year": year,
        "publisher": publisher,
        "address": address
    })

    db.session.commit()

def create_article(key, title, author, year, journal, pages, volume, month, doi):
    sql = text("""
        INSERT INTO Articles
        (key, title, author, year, journal, pages, volume, month, doi)
        VALUES
        (:key, :title, :author, :year, :journal, :pages, :volume, :month, :doi)
    """)

    db.session.execute(sql, {
        "key": key,
        "title": title,
        "author": author,
        "year": year,
        "journal": journal,
        "pages": pages,
        "volume": volume,
        "month": month,
        "doi": doi
    })

    db.session.commit()

def get_articles():
    result = db.session.execute(text("""
        SELECT id, key, title, author, year,
               journal, pages, volume, month, doi
        FROM Articles
    """))

    articles = result.fetchall()

    return [
        Article(
            article[0], article[1], article[2], article[3],
            article[4], article[5], article[6], article[7],
            article[8], article[9]
        )
        for article in articles
    ]
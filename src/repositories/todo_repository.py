from config import db
from sqlalchemy import text
from entities.article import Article
from entities.book import Book

def get_books():
    result = db.session.execute(text("""
        SELECT id, key, title, author, year, publisher, address
        FROM Books
    """))
    books = result.fetchall()
    return [
        Book(
            book[0], book[1], book[2], book[3],
            book[4], book[5], book[6]
        )
        for book in books
    ]

def create_book(key, title, author, year, publisher, address):
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

def get_book(book_id):
    sql = text("""
            SELECT id, key, title, author, year, publisher, address
            FROM Books WHERE id = :id
        """)
    result = db.session.execute(sql, {"id": book_id})
    book = result.fetchone()
    return book

def update_book(book_id, key, title, author, year, publisher, address):
    sql = text("""
            UPDATE Books SET key = :key, title = :title, author = :author, year = :year, publisher = :publisher, address = :address
            WHERE id = :id
        """)
    db.session.execute(sql, {
        "key": key,
        "title": title,
        "author": author,
        "year": year,
        "publisher": publisher,
        "address": address,
        "id": book_id
        })
    db.session.commit()

def get_article(article_id):
    sql = text("""
            SELECT id, key, title, author, year, journal, pages, volume, month, doi
            FROM Articles WHERE id = :id
        """)
    result = db.session.execute(sql, {"id": article_id})
    article = result.fetchone()
    return article

def update_article(article_id, key, title, author, year, journal, pages, volume, month, doi):
    sql = text("""
            UPDATE Articles SET key = :key, title = :title, author = :author, year = :year, journal = :journal, pages = :pages, volume = :volume, month = :month, doi = :doi
            WHERE id = :id
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
        "doi": doi,
        "id": article_id
        })
    db.session.commit()

def remove_book(book_id):
    sql = text("""
            DELETE FROM Books WHERE id = :id
            """)
    db.session.execute(sql, {
            "id": book_id})
    db.session.commit()

def remove_article(article_id):
    sql = text("""
            DELETE FROM Articles WHERE id = :id
            """)
    db.session.execute(sql, {
            "id": article_id})
    db.session.commit()
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

def find_citation(query):

    like = "%" + query + "%"
    books_sql = text("""SELECT id, key, title, author, year, publisher, address
            FROM Books WHERE key
             LIKE :cond OR title LIKE :cond OR author LIKE :cond 
             OR year LIKE :cond OR publisher LIKE :cond OR address LIKE :cond
             ORDER BY id DESC
            """)
    books_result = db.session.execute(books_sql, {"cond": like}).fetchall()
    books = [
        Book(
            book[0], book[1], book[2], book[3],
            book[4], book[5], book[6]
        )
        for book in books_result
    ]

    articles_sql = text("""SELECT id, key, title, author, year,
                journal, pages, volume, month, doi
                FROM Articles WHERE key
                LIKE :cond OR title LIKE :cond OR author LIKE :cond 
                OR year LIKE :cond OR journal LIKE :cond OR pages LIKE :cond
                OR volume LIKE :cond OR month LIKE :cond OR doi LIKE :cond
                ORDER BY id DESC
                """)
    articles_result = db.session.execute(articles_sql, {"cond": like}).fetchall()

    articles = [Article(
                article[0], article[1], article[2], article[3],
                article[4], article[5], article[6], article[7],
                article[8], article[9]
            )
            for article in articles_result
        ]
    return {"books": books,
        "articles": articles}

def get_tags():
    sql = text("""
        SELECT id, name FROM Tags
        ORDER BY name
    """)
    result = db.session.execute(sql).fetchall()

    return [
        {"id": tag[0], "name": tag[1]}
        for tag in result
    ]


def create_tag(name):
    name = name.strip()

    if not name:
        return None

    sql = text("""
        INSERT OR IGNORE INTO Tags (name)
        VALUES (:name)
    """)
    db.session.execute(sql, {"name": name})
    db.session.commit()

    result = db.session.execute(
        text("SELECT id FROM Tags WHERE name = :name"),
        {"name": name}
    ).fetchone()

    return result[0]


def delete_tag(tag_id):
    db.session.execute(
        text("DELETE FROM BookTags WHERE tag_id = :tag_id"),
        {"tag_id": tag_id}
    )
    db.session.execute(
        text("DELETE FROM ArticleTags WHERE tag_id = :tag_id"),
        {"tag_id": tag_id}
    )
    db.session.execute(
        text("DELETE FROM Tags WHERE id = :tag_id"),
        {"tag_id": tag_id}
    )
    db.session.commit()


def get_book_tags(book_id):
    sql = text("""
        SELECT Tags.id, Tags.name
        FROM Tags
        JOIN BookTags ON Tags.id = BookTags.tag_id
        WHERE BookTags.book_id = :book_id
        ORDER BY Tags.name
    """)
    result = db.session.execute(sql, {"book_id": book_id}).fetchall()

    return [
        {"id": tag[0], "name": tag[1]}
        for tag in result
    ]


def get_article_tags(article_id):
    sql = text("""
        SELECT Tags.id, Tags.name
        FROM Tags
        JOIN ArticleTags ON Tags.id = ArticleTags.tag_id
        WHERE ArticleTags.article_id = :article_id
        ORDER BY Tags.name
    """)
    result = db.session.execute(
        sql, {"article_id": article_id}
    ).fetchall()

    return [
        {"id": tag[0], "name": tag[1]}
        for tag in result
    ]


def set_book_tags(book_id, tag_ids):
    db.session.execute(
        text("DELETE FROM BookTags WHERE book_id = :book_id"),
        {"book_id": book_id}
    )

    for tag_id in set(tag_ids):
        db.session.execute(text("""
            INSERT OR IGNORE INTO BookTags (book_id, tag_id)
            SELECT :book_id, id FROM Tags WHERE id = :tag_id
        """), {
            "book_id": book_id,
            "tag_id": tag_id
        })

    db.session.commit()


def set_article_tags(article_id, tag_ids):
    db.session.execute(
        text("DELETE FROM ArticleTags WHERE article_id = :article_id"),
        {"article_id": article_id}
    )

    for tag_id in set(tag_ids):
        db.session.execute(text("""
            INSERT OR IGNORE INTO ArticleTags (article_id, tag_id)
            SELECT :article_id, id FROM Tags WHERE id = :tag_id
        """), {
            "article_id": article_id,
            "tag_id": tag_id
        })

    db.session.commit()
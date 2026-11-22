from flask import redirect, render_template, request, jsonify, flash, Flask, Response
from db_helper import reset_db
from repositories.todo_repository import get_books, get_articles, create_book, create_article, get_book, update_book, get_article, update_article, remove_book, remove_article
from config import app, test_env
import calendar

@app.route("/")
def index():
    books = get_books()
    articles = get_articles()

    books_order = request.args.get("books_order", "asc")
    articles_order = request.args.get("articles_order", "asc")
    selected_book_id = request.args.get("book", type=int)
    selected_article_id = request.args.get("article", type=int)

    selected_book = next(
        (book for book in books if book.id == selected_book_id),
        None
    )

    selected_article = next(
        (article for article in articles if article.id == selected_article_id),
        None
    )

    books = sorted(
        books,
        key=lambda book: book.title.casefold(),
        reverse=(books_order == "desc")
    )

    articles = sorted(
        articles,
        key=lambda article: article.title.casefold(),
        reverse=(articles_order == "desc")
    )

    return render_template(
        "index.html",
        books=books,
        articles=articles,
        books_order=books_order,
        articles_order=articles_order,
        selected_book=selected_book,
        selected_book_id=selected_book_id,
        selected_article=selected_article,
        selected_article_id=selected_article_id
    )

@app.route("/new_book")
def new():
    return render_template("new_book.html")
@app.route("/new_article")
def new_article():
    return render_template("new_article.html")

@app.route("/create_book", methods=["POST"])
def books_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    publisher = request.form.get("publisher")
    address = request.form.get("address")

    try:
        if not all([key, author, title, year, publisher]):
            raise ValueError("Please fill in all required fields")

        create_book(key, title, author, year, publisher, address)

        return redirect("/")

    except Exception as error:
        flash(str(error))
        return redirect("/new_book")
    
@app.route("/create_article", methods=["POST"])
def article_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    journal = request.form.get("journal")
    pages = request.form.get("pages")
    volume = request.form.get("volume")
    month = request.form.get("month")
    doi = request.form.get("doi")

    months = list(calendar.month_name[1:])
    months_abbreviated = ["Sept." if month_name == "September" else f"{month_name[:3]}." if len(month_name) > 4 else month_name for month_name in months]

    try:
        if not all([key, author, title, year, journal]):
            raise ValueError("Please fill in all required fields")
    
        if not all([key.strip(), author.strip(), title.strip(), year.strip(), journal.strip()]):
            raise ValueError("Must not contain only spaces")
        
        if len(year) != 4 or not year.isdigit():
            raise ValueError("Enter only 4 digits")
        
        if volume and not volume.isdigit():
            raise ValueError("Invalid volume")
        
        if month and (not month.strip() or (month not in months and month not in months_abbreviated)):
            raise ValueError("Invalid month")
        
        if pages and (not pages.strip() or not any(page.isdigit() for page in pages)):
            raise ValueError("Invalid pages")
        
        if doi and (not doi.strip() or not "10." in doi or not "/" in doi):
            raise ValueError("invalid doi")

    # Tallennetaan artikkeli tietokantaan
        create_article(key, title, author, year, journal, pages, volume, month, doi)
        return redirect("/")
    
    except Exception as error:
        flash(str(error))
        return redirect("/new_article")

@app.route("/edit_book/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = get_book(book_id)

    if request.method == "GET":
        return render_template("edit_book.html", book=book)
    if request.method == "POST":
        key = request.form.get("key")
        author = request.form.get("author")
        title = request.form.get("title")
        year = request.form.get("year")
        publisher = request.form.get("publisher")
        address = request.form.get("address")

        try:
            if not all([key, author, title, year, publisher]):
                raise ValueError("Please fill in all required fields")

            update_book(book_id, key, title, author, year, publisher, address)

            return redirect("/")

        except Exception as error:
            flash(str(error))
            return redirect(f"/edit_book/{book_id}")

@app.route("/edit_article/<int:article_id>", methods=["GET", "POST"])
def edit_article(article_id):
    article = get_article(article_id)

    if request.method == "GET":
        return render_template("edit_article.html", article=article)
    if request.method == "POST":
        key = request.form.get("key")
        author = request.form.get("author")
        title = request.form.get("title")
        year = request.form.get("year")
        journal = request.form.get("journal")
        pages = request.form.get("pages")
        volume = request.form.get("volume")
        month = request.form.get("month")
        doi = request.form.get("doi")
        months = list(calendar.month_name[1:])
        months_abbreviated = ["Sept." if month_name == "September" else f"{month_name[:3]}." if len(month_name) > 4 else month_name for month_name in months]

        try:
            if not all([key, author, title, year, journal]):
                raise ValueError("Please fill in all required fields")
                
            if not all([key.strip(), author.strip(), title.strip(), year.strip(), journal.strip()]):
                raise ValueError("Must not contain only spaces")
                    
            if len(year) != 4 or not year.isdigit():
                raise ValueError("Enter only 4 digits")
                    
            if month and (not month.strip() or (month not in months and month not in months_abbreviated)):
                raise ValueError("Invalid month")
                    
            if volume and not volume.isdigit():
                raise ValueError("Invalid volume")
                    
            if doi and (not doi.strip() or not "10." in doi or not "/" in doi):
                raise ValueError("invalid doi")
            
            update_article(article_id, key, title, author, year, journal, pages, volume, month, doi)
            return redirect("/")

        except Exception as error:
            flash(str(error))
            return redirect(f"/edit_article/{article_id}")

@app.route("/remove_book/<int:book_id>", methods=["GET", "POST"])
def delete_book(book_id):
    book = get_book(book_id)

    if request.method == "GET":
        return render_template("remove_book.html", book=book)

    if request.method == "POST":
        if "continue" in request.form:
            remove_book(book_id)
        return redirect("/")

@app.route("/remove_article/<int:article_id>", methods=["GET", "POST"])
def delete_article(article_id):
    article = get_article(article_id)

    if request.method == "GET":
        return render_template("remove_article.html", article=article)

    if request.method == "POST":
        if "continue" in request.form:
            remove_article(article_id)
        return redirect("/")
    
@app.route("/download")
def download():
    books = get_books()
    articles = get_articles()

    file_content = """"""

    for book in books:
        file_content += f"""
@book{{{book.key},
    author = {{{book.author}}},
    title = {{{book.title}}},
    publisher = {{{book.publisher}}},
    year = {{{book.year}}},
    address = {{{book.address}}}
    
}}"""

    for article in articles:
        file_content += f"""
@book{{{article.key},
    author = {{{article.author}}},
    title = {{{article.title}}},
    journal = {{{article.journal}}},
    year = {{{article.year}}},
    volume = {{{article.volume}}},
    pages = {{{article.pages}}},
    month = {{{article.month}}},
    doi = {{{article.doi}}}

}}"""

    return Response(file_content, mimetype="application/x-bibtex", headers={"Content-Disposition": "attachment; filename=references.bib"})

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })

if __name__ == "__main__":
    app.run(debug=True)

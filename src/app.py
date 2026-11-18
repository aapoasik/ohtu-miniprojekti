from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_books, get_articles, create_book, create_article
from config import app, test_env
import calendar

@app.route("/")
def index():
    books = get_books()
    articles = get_articles()
    return render_template("index.html", books=books, articles=articles)

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
    months_abbreviated = [f"{month[:4]}." if len(month) > 4 else month for month in months]

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
# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })

if __name__ == "__main__":
    app.run(debug=True)

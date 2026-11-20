from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_todos, get_articles, create_todo, create_article
from config import app, test_env

@app.route("/")
def index():
    todos = get_todos()
    articles = get_articles()

    books_order = request.args.get("books_order", "asc")
    articles_order = request.args.get("articles_order", "asc")

    todos = sorted(
        todos,
        key=lambda todo: todo.title.casefold(),
        reverse=(books_order == "desc")
    )

    articles = sorted(
        articles,
        key=lambda article: article.title.casefold(),
        reverse=(articles_order == "desc")
    )

    return render_template(
        "index.html",
        todos=todos,
        articles=articles,
        books_order=books_order,
        articles_order=articles_order
    ) 
@app.route("/new_todo")
def new():
    return render_template("new_todo.html")

@app.route("/new_article")
def new_article():
    return render_template("new_article.html")

@app.route("/create_todo", methods=["POST"])
def todo_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    publisher = request.form.get("publisher")
    address = request.form.get("address")

    try:
        if not all([key, author, title, year, publisher]):
            raise ValueError("Please fill in all required fields")

        create_todo(key, title, author, year, publisher, address)

        return redirect("/")

    except Exception as error:
        flash(str(error))
        return redirect("/new_todo")
    
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

    try:
        if not all([key, author, title, year, journal]):
            raise ValueError("Please fill in all required fields")
    
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